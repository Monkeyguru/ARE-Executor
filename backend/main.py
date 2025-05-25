from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"ARE": "Autonomous Real-time Executor is alive"}

