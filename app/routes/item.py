from fastapi import APIRouter,HTTPException
from app.database.session import fake_db
from app.schemas.item import UpdateItem,Item
from typing import Any
from app.crud.item import create,read,update,delete

# creating router for item
route=APIRouter()

# root url 
@route.get('/')
def root():
    return {"message":"Hello World"}

# url to create an Item object.
# first it checks if the item with the given id is present or not if present thows as HTTP exception otherwise creates an Item object and returns it.
@route.post('/items')
def create_item(item:Item)->Item:
    try:
        return create.create(item,fake_db)
    except:
        raise HTTPException(detail="This item is already  present in our database",status_code=400)

# url to retrive all the items in our database
@route.get('/items')
def get_all_items()->dict[Any,Item]:
    return read.get_all_items(fake_db)

# url to retrive perticular item
# first it checks if the item with the given id is present or not if present returns the Item,otherwise thows a HTTP exception.
@route.get('/items/{id}')
def get_item(id:int)->Item:
    try:
        return read.get_item(id,fake_db)
    except:
        raise HTTPException(status_code=404 , detail="Item not found put error")

# url to update an Item with specific id .
# first it checks if the item with the given id is present or not if present updates the requested fields and return the updated object otherwise throws HTTP exception.
@route.put('/items/{id}')
def update_item(id:int,item:UpdateItem)->Item:
    try:
        return update.update(id,item,fake_db)
    except:
        raise HTTPException(status_code=404 , detail="Item not found put error")

#url to delete item with specific id.
# first it checks if the item with the given id is present or not if present deletes the  object otherwise throws HTTP exception.
@route.delete('/items/{id}')
def delete_item(id:int):
    try:
        return delete.delete(id,fake_db)
    except:
        raise HTTPException(status_code=404,detail="Item not found delete error")
