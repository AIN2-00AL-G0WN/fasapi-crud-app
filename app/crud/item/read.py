from sqlalchemy.orm import session
from app.models.item import Item as item_model

# function to retrive all the items in our database
def get_all(db:session):
    return db.query(item_model).all()


# function to retrive perticular item which takes id and db session.
# first it checks if the item with the given id is present or not if present returns the Item,otherwise thows an exception.
def get(db:session,id:int):
    return db.query(item_model).get(id)