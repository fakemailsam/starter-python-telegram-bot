from fastapi import FastAPI, Header, HTTPException, Depends


app = FastAPI()

@app.get("/items/")
def read_root():
    return 'hello'
