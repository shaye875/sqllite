from pydantic import BaseModel
class Update(BaseModel):
    id:int
    name:str
    grade:int