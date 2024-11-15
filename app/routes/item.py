from sqlalchemy.orm import session
from app.database.session import get_db
from app.crud.item.create import create
from app.crud.item.read import get,get_all
from app.crud.item.update import update
from app.crud.item.delete import delete
from app.schemas.item import CreateItem,UpdateItem,Item
from fastapi import APIRouter,HTTPException,Depends
from typing import List

# creating router for item
route=APIRouter()

# root url 
@route.get('/')
def root():
    return {"message":"Hello World"}

# url to create an Item object.
# first it checks if the item with the given id is present or not if present thows as HTTP exception otherwise creates an Item object and returns it.
@route.post('/items')
def create_item(item:CreateItem,db:session=Depends(get_db))->Item:
    try:
        return create(db=db,item=item)
    except:
        raise HTTPException(status_code=400, detail="Item with this name or Id already exists in our Database.")

# url to retrive all the items in our database
@route.get('/items')
def get_all_items(db:session=Depends(get_db))->List[Item]:
    try:
        return get_all(db)
    except:
        raise HTTPException(status_code=500,detail="Internal server Error!")

# url to retrive perticular item
# first it checks if the item with the given id is present or not if present returns the Item,otherwise thows a HTTP exception.
@route.get('/items/{id}')
def get_item(id:int,db:session=Depends(get_db))->Item:
    try:
       return get(db=db,id=id)
    except:
        raise HTTPException(status_code=404, detail=f"Item not found get error")

# url to update an Item with specific id .
# first it checks if the item with the given id is present or not if present updates the requested fields and return the updated object otherwise throws HTTP exception.
@route.put('/items/{id}')
def update_item(id:int,item:UpdateItem,db:session=Depends(get_db))->Item:
    try:
        return update(db=db,id=id,item_update=item)
    except:
        raise HTTPException(status_code=404, detail=f"Item not found get error")

#url to delete item with specific id.
# first it checks if the item with the given id is present or not if present deletes the  object otherwise throws HTTP exception.
@route.delete('/items/{id}')
def delete_item(id:int,db:session=Depends(get_db))->dict:
    try:
        delete(db=db,id=id)
        return {"message":f"Item with id {id} deleted successfully!!"}
    except:
        raise HTTPException(status_code=404, detail=f"Item not found get error")