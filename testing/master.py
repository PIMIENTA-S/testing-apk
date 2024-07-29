from fastapi import FastAPI

master = FastAPI()

@master.get("/")
def testing():
    return "hola"