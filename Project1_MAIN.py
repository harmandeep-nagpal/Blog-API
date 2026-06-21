# We need to install pip install fastapi uvicorn sqlachemy psycopg2-binary python-dotenv

from fastapi import FastAPI 
from Project1_DATABASE import engine 
import Project1_MODEL as models

models.Base.metadata.create_all(bind=engine) 
# Explanation in 24

app = FastAPI()

@app.get("/")
def home():
    return{
        "message" : "Blog API Started"
    }

