from fastapi import FastAPI, Header, HTTPException, Depends


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
