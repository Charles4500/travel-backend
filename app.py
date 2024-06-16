from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from models.tickets import Ticket
from models.customers import Customer
from models.hire import Hire
from models.bus import Buses
from front import PrivateModel, PublicModel


app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=[
    "*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hire")
def get_cars():
    cars = Hire.find_all()

    return cars


@app.post("/hire")
def save(data: PrivateModel):
    hire = Hire(data.name, data.car_brand, data.image,
                data.hire_fee, data.date_hire)
    hire.save()
    return hire.to_dict()


@app.get("/bus")
def get_buses():
    buses = Buses.find_all_buses()

    return buses


@app.post("/bus")
def save(data: PublicModel):
    bus = Buses(data.name, data.location_from,
                data.location_to, data.passengers, data.price)

    return bus.to_dict()


        
