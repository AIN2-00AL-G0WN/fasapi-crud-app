from app.schemas.item import Item
from fastapi.encoders import jsonable_encoder

# this function takes Item id and db session as parameter
# it checks for ihe item with given id. If present updates the item and returns the updated Item otherwise throws an exception.
def update(id:int,item,db)->Item:
    if id in db:
        db_item_data=  db[id]
        db_item_model= Item(**db_item_data)
        updated_data= item.dict(exclude_unset=True)
        updated_item= db_item_model.copy(update=updated_data)
        db[id]=  jsonable_encoder(updated_item)
        return updated_item
    raise FileExistsError(detail="Item not found")