from sqllite1 import *
from fastapi import FastAPI
import uvicorn
from table import *
from update import *
app = FastAPI()

@app.get("/")
def get_all():
    return select()

@app.post("/insert")
def table(table:Table):
    inset(table.name,table.grade)
    return {"the insert":True}

@app.put("/update")
def set(row:Update):
    update(row.id,row.name,row.grade)
    return {"data is chainge":True}

@app.delete("/delete/{id}")
def del_row(id):
    delete(id)
    return {"the row is del":True}