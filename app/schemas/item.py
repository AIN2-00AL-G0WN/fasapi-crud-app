# Schema for pydantic model
# importing pydantic Base model as parent which is inherited by all the model classes
from pydantic import BaseModel
from typing import Optional

#class to create Item model
class Item(BaseModel):
    id:int
    name:str
    description:Optional[str]=None
    price:float
    quantity:int


# class to update the model.
# only description, price and quantity of the model can be modeified all these fields are optional
class UpdateItem(BaseModel):
    description:Optional[str]=None
    price:Optional[float]=None
    quantity:Optional[int]=None
