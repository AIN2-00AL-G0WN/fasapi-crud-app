# importing Item pydantic model from schemas
from app.schemas.item import Item 

# Dictionary as fake database  with 2 Item object as initial data
fake_db={1:Item(id=1,description="first smartphone with 100MP camera",name="VIVO",price=20000,quantity=17),
         2:Item(id=2,description="new cooling system for better gaming experience",name="ASUS",price=40000,quantity=3)}