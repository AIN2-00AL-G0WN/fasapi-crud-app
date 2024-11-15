from sqlalchemy.orm import session
from app.models.item import Item as item_model
from app.schemas.item import CreateItem as create_item_schema

# this function takes Item object and db session. 
# checks for Item with given name if present throws an exception otherwise creates the Item and return it.
def create(db:session,item:create_item_schema):
    db_item=item_model(name=item.name,description=item.description,price=item.price,quantity=item.quantity)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item