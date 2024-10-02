from fastapi import FastAPI
import uvicorn

from src.routes import main_router

app = FastAPI()

app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)