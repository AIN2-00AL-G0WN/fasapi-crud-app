from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    id:int
    name:str
    description:Optional[str]=None
    price:float
    quantity:int

    class Config:
        orm_mode = True

class CreateItem(ItemBase):
    pass

class Item(ItemBase):
    pass

class UpdateItem(BaseModel):
    description:Optional[str]=None
    price:Optional[float]=None
    quantity:Optional[int]=None

    class Config:
        orm_mode=True
