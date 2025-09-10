from fastapi import FastAPI
from model.service.calculadora import Calculadora 

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello" : "world"}

@app.get("/vaimeufi")
def  root ():
    return {"nota": "2"}


@app.get("/somar/{valor_1}/{valor_2}")
async def somar (valor_1 :int,valor_2 :int ):
   calc = Calculadora()
   resultado = calc.somar(valor_1, valor_2)
   return {"resultado" : resultado}
