from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is working!"}

@app.get("/test")
async def root():
    return {"message": "Test route"}
