from sqlalchemy import Column,INTEGER,FLOAT,String
from app.database.session import Base,engine

# Python class to create Item object and also the schema for item table
class Item(Base):
    __tablename__ = "item"

    id = Column(INTEGER, primary_key=True)  # Primary key
    name = Column(String,unique=True)  # Name of the item, must be unique
    description = Column(String, nullable=True) # Item description, can be null
    price=Column(FLOAT) # Item price
    quantity=Column(INTEGER)   # Item Quantity

# binds the model to the database and creates all the fields in our database
Base.metadata.create_all(engine)