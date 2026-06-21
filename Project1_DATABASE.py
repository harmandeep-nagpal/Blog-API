from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# Explanation of each import in 23

# DATABASE_URL = "postgresql://username:password@localhost/nameofdatabase" 
DATABASE_URL = "postgresql://postgres:Harman01633%40@localhost/blogdb" 

# IMPORTANT -> while i was typing password Harman01633@ then i must URL-encode the @ part as %40 

# Username is generally postgres and password is set during the installation of Postgresql and name of database can be whatever we keep

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine) 
Base = declarative_base()