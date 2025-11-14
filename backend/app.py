from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Whalley Backend Running"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )