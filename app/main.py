from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "CI/CD Pipeline Running Successfully"}

@app.get("/health")
def health():
    return {"status": "healthy"}