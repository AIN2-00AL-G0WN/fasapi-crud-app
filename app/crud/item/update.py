from sqlalchemy.orm import session
from app.models.item import Item as item_model
from app.schemas.item import UpdateItem as update_item_schema

# this function takes Item id, db session and item_update as parameter
# it checks for ihe item with given id. If present updates the item and returns the updated Item otherwise throws an exception.
def update(db:session,id:int,item_update:update_item_schema):
    db_item=db.query(item_model).get(id)

    if item_update.description is not None:
        db_item.description=item_update.description

    if item_update.price is not None:
        db_item.price=item_update.price

    if item_update.quantity is not None:
        db_item.quantity=item_update.quantity
    db.commit()
    db.refresh(db_item)
    return db_item