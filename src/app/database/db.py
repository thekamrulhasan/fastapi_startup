from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

# Replace these values with your actual database information
db_user = os.environ.get("db_user")
db_password = os.environ.get("db_password")
db_host = os.environ.get("db_host")
db_name = os.environ.get("db_name")


# Construct the updated DATABASE_URL
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()
