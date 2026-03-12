from fastapi import FastAPI
from app.controller.meter_controller import router


app = FastAPI(title="GridTariff API")

app.include_router(router)