from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return"THIS IS A HOME PAGE"

@app.get("/add")
async def add():
    num1 = 20
    num2 = 40
    return num1+num2

@app.get("/addinput")
async def addWithInput(num1:int,num2:int):
    num1+num2
