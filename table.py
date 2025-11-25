from pydantic import BaseModel
class Table(BaseModel):
    name:str
    grade:int