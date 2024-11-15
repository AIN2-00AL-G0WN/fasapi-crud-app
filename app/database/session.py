import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import  load_dotenv


# loading environment variables  
load_dotenv()

# Database connection key storen in .env file
DATABASE_CONNECTION_URL=os.getenv("DATABASE_CONNECTION_URL")

# Creating a sqlalchemy engine to establish connection with the database
engine = create_engine(DATABASE_CONNECTION_URL)

# creating a sqlalchemy session to handle transactions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)



def get_db():
    db = SessionLocal()  # Creates a new database session
    try:
        yield db  # used here to return the session
    finally:
        db.close() # closes the session