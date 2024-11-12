from fastapi import APIRouter,HTTPException
from app.database.session import fake_db
from app.schemas.item import CreateItem,UpdateItem,Item
from typing import List,Any
from fastapi.encoders import jsonable_encoder
# creating router for item
route=APIRouter()

# root url 
@route.get('/')
def root():
    return {"message":"Hello World"}
# url to create an Item object.
# first it checks if the item with the given id is present or not if present thows as HTTP exception otherwise creates an Item object and returns it.
@route.post('/items')
def create_item(item:CreateItem)->Item:
    if item.id in fake_db:
        raise HTTPException(status_code=400,detail="Item with this name or Id already exists in our Database.")
    fake_db[item.id]=jsonable_encoder(item)
    return item

# url to retrive all the objects in our database
@route.get('/items')
def get_all_items()->dict[Any,Any]:
    return fake_db

# url to update an Item with specific id .
# first it checks if the item with the given id is present or not if present updates the requested fields and return the updated object otherwise throws HTTP exception.
@route.put('/items/{id}')
def update_item(id:int,item:UpdateItem)->Item:
    if id in fake_db:
        db_item_data=  fake_db[id]
        db_item_model= CreateItem(**db_item_data)
        updated_data= item.dict(exclude_unset=True)
        updated_item= db_item_model.copy(update=updated_data)
        fake_db[id]=  jsonable_encoder(updated_item)
        return updated_item
    raise HTTPException(status_code=404 , detail="Item not found put error")

#url to delete item with specific id.
# first it checks if the item with the given id is present or not if present deletes the  object otherwise throws HTTP exception.
@route.delete('/items/{id}')
def delete_item(id:int):
    if id in fake_db:
        del fake_db[id]
        return {"message": "Item deleted successfully."}
    raise HTTPException(status_code=404,detail="Item not found delete error")
