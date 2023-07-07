import uvicorn
from fastapi import FastAPI

from app.controllers.email_controller import router

app = FastAPI(
    title="ASADAL PAY",
    version="0.1"
)


@app.get("/")
def get_main():
    return {"Hello": "World"}


app.include_router(router=router)
