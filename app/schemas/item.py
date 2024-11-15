from pydantic import BaseModel
from typing import Optional


# model to create Item
class CreateItem(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

    class Config:
        orm_mode = True  # to serialize and deserialize sql models

# Item model
class Item(BaseModel):
    id:int
    name: str
    description: Optional[str] = None
    price: float
    quantity: int

    class Config:
        orm_mode = True  # to serialize and deserialize sql models

# class to update the model.
# only description, price and quantity of the model can be modeified all these fields are optional
class UpdateItem(BaseModel):
    description:Optional[str]=None
    price:Optional[float]=None
    quantity:Optional[int]=None

    class Config:
        orm_mode=True  # to serialize and deserialize sql models
