
from fastapi import FastAPI  
from models import Product
app = FastAPI()
@app.get("/")
def greet():
    return "welcome to hello world"
   
# id: int 
    name:str 
    desription:str 
    price: float 
    quantity: int 


products=[
    Product(id=11,name="apple",desription="budget phone",price=99.99,quantity=10),
    Product(id=21,name="realme",desription="phone",price=998.99,quantity=22),
    Product(id=22,name="samsong",desription="phone",price=998.99,quantity=25),
    Product(id=23,name="apple",desription="watch",price=998.99,quantity=26)

]
@app.get("/products")
def get_all_products():
    #create data base connection 
    # write query
    return products

@app.get("/product/{id}")
def get_all_products_by_id(id:int):
    for Product in products :
        if Product.id == id:
            return Product
    return "product id is not found" 

@app.post("/product")
def add_product(product:Product):
    products.append(Product)
    return products 

@app.put("/product")
def update_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product 
            return "Product added succesfully" 

@app.delete("/product")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
    return "Product Delete"

