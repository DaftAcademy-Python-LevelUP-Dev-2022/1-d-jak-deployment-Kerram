from fastapi import FastAPI, Response

app = FastAPI()


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
