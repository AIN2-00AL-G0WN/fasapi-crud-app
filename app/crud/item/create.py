from fastapi.encoders import jsonable_encoder

def create(item,db):
    if item.id not in db:
        db[item.id]=jsonable_encoder(item)
        return item
    raise ValueError("Item with this name or Id already exists in our Database.")