from sqlalchemy import Column, Integer , String, Text
from Project1_DATABASE import Base 

# "Go to the file Project1_DATABASE.py, find something named Base, and bring it into this file."
# --------------------------------------------------------------------------------------------------------------

# IMPORTANT INTERPERTATION -> Firstly i was trying to bind 102_Project1_DATABASE but it was throwing error because i came to know that because Python interprets: 102_Project2_DATABASE import base as if 102 were a number, and not a valid file name so we had to edit it 

#BLOG table 
# We inherit from base ,Explanation -> 24

class Blog(Base): # Python allows blog, but by convenyion model classes start with a capital letter:
    __tablename__ = "blogs"
    id = Column(Integer, primary_key = True , index = True)
    title = Column(String)
    content = Column(Text)

# How do we check our newly created table -> Go to pgadmin4 -> blogdb -> Schemas -> public-> tables -> Blogs -> Column
