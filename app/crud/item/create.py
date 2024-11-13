from fastapi.encoders import jsonable_encoder
from app.schemas.item import Item

# this function takes Item object and db session. 
# checks for Item with given id if present throws an exception otherwise creates the Item and return it.
def create(item:Item,db)->Item:
    if item.id not in db:
        db[item.id]=jsonable_encoder(item)
        return item
    raise ValueError("Item with this name or Id already exists in our Database.")