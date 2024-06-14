from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.hire import Hire

from front import CatalogueModel


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=[
    "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/buses")
def get_buses():
    return [{"bus": "easy coach"}]


@app.get("/rent")
def get_cars():
    pass


@app.post("/hire")
def save_cars(data: CatalogueModel):
    hire = Hire(**data)
    hire.save()
    return hire.to_dict()
