from pydantic import BaseModel


class CatalogueModel(BaseModel):
    name: str
    car_brand: str
    image : str
    hire_fee: int
    date_hire : str
