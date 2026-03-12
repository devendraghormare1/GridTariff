from fastapi import APIRouter, HTTPException
from app.services.meter_service import fetch_meter_data, fetch_all_meters

router = APIRouter()


@router.get("/meters/{meter_id}")
def get_meter(meter_id: str):

    data = fetch_meter_data(meter_id)

    if not data:
        raise HTTPException(status_code=404, detail="Meter not found")
    
    return data

@router.get("/meters")
def list_meters():
    return fetch_all_meters()