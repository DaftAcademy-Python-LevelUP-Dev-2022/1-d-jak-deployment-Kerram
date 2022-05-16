from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"start": "1970-01-01"}