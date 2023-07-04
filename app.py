from fastapi import FastAPI
import sys

# Set disallow pycache
sys.dont_write_bytecode = True

# Instance of fatsapi app
app = FastAPI()


# Home api route
@app.get("/")
def index():
    return {"Message": "Welcome..."}
