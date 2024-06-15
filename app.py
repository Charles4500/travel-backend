from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.hire import Hire
from models.buses import Buses
from front import CatalogueModel, BusesModel


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=[
    "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/public")
def get_buses():
    pass


@app.post('/public')
def save(data: BusesModel):
    buses = Buses(data.name, data.location_from,
                  data.location_to, data.passengers, data.price)
    buses.save()


@app.get("/hire")
def get_cars():
    cars = Hire.find_all()

    return cars


@app.post("/hire")
def save(data: CatalogueModel):
    hire = Hire(data.name, data.car_brand, data.image,
                data.hire_fee, data.date_hire)
    hire.save()
    return hire.to_dict()
