from app.schemas.item import Item

# this function takes an id and db session. 
# checks for Item with given id if present deletes the Item and return a success message  otherwise throws an exception.
def delete(id:Item,db)-> dict:
    if id in db:
        del db[id]
        return {"message": "Item deleted successfully."}
    raise FileExistsError(f"Item with id {id} not found in our database")