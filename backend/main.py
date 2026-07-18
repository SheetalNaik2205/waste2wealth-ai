from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Waste2Wealth AI backend is running!"}