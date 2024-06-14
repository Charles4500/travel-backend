
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/buses")
def get_buses():
    return [{"bus": "easy coach"}]
