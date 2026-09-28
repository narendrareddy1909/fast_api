#  ppydantic use for validation 
from pydantic import BaseModel
class Product(BaseModel):
    id: int 
    name:str 
    desription:str 
    price: float 
    quantity: int 
