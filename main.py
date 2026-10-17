from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "message":"Hi, Hello From Pratik Deshmukh"
    }

@app.get("/about")
def about():
    return {
        "about":"A ML Engg....",
        "Name":"Pratik Deshmukh"
    }