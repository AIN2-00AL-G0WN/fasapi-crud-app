from sqlalchemy.orm import session
from app.models.item import Item as item_model
from app.schemas.item import CreateItem as create_item_schema,UpdateItem as update_item_schema

# this function takes an id and db session. 
# checks for Item with given id if present deletes the Item otherwise throws an exception.
def delete(db:session,id:int):
    item=db.query(item_model).get(id)
    db.delete(item)
    db.commit()