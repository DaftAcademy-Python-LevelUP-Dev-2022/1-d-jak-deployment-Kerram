from fastapi import FastAPI, Response
from pydantic import BaseModel
from multiprocessing import Lock
import datetime

app = FastAPI()
lock = Lock()
event_id = 0


class Event(BaseModel):
    date: str
    event: str


class StoredEvent(BaseModel):
    id: int
    date: str
    name: str
    date_added: str


@app.get("/")
def root():
    return {"start": "1970-01-01"}


@app.get("/method")
def method_get():
    return {"method": "GET"}


@app.post("/method", status_code=201)
def method_post():
    return {"method": "POST"}


@app.delete("/method")
def method_delete():
    return {"method": "DELETE"}


@app.put("/method")
def method_put():
    return {"method": "PUT"}


@app.options("/method")
def method_options():
    return {"method": "OPTIONS"}


@app.get("/day")
def validate_day_number(name: str, number: int):
    days = {
        "monday": 1,
        "tuesday": 2,
        "wednesday": 3,
        "thursday": 4,
        "friday": 5,
        "saturday": 6,
        "sunday": 7,
    }

    if (name in days) and (days[name] == number):
        return Response(status_code=200)
    return Response(status_code=400)


@app.put("/events")
def events(event: Event):
    global event_id
    # Taken from https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
    try:
        datetime.datetime.strptime(event.date, '%Y-%m-%d')
    except ValueError:
        return Response(status_code=400)

    try:
        lock.acquire()
        local_event_id = event_id
        event_id += 1
    finally:
        lock.release()

    return StoredEvent(id=local_event_id, date=event.date, name=event.event, date_added=datetime.date.today().strftime('%Y-%m-%d'))
