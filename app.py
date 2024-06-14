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


# @app.get("/buses")
# def get_buses():


@app.get("/hire")
def get_cars():
    return [{"bus": "easy coach"}]


@app.post("/hire")
def save(data: CatalogueModel):
    hire = Hire(data.name, data.car_brand, data.image,
                data.hire_fee, data.date_hire)
    hire.save()
    return hire.to_dict()
