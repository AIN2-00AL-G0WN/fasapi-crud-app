from typing import List,Any
from app.schemas.item import Item
# function to retrive all the items in our database
def get_all_items(db)->dict[Any,Item]:
    return db


# function to retrive perticular item which takes id and db session.
# first it checks if the item with the given id is present or not if present returns the Item,otherwise thows a HTTP exception.
def get_item(id:int,db)->Item:
    if id in db:
        return db[id]
    raise FileExistsError("Item not found")