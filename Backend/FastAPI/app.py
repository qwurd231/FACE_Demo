from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")

def hello():
    return {"hello": "world"}

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8000)