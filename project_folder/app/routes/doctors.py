# app/routes/doctors.py
from fastapi import APIRouter, Depends

from app.models import User
from ..authentication import get_current_user
from ..services.doctor_service import send_patient_info

router = APIRouter()

@router.post("/send-patient-info")
async def send_patient_information(patient_id: int, doctor_id: int, current_user: User = Depends(get_current_user)):
    await send_patient_info(patient_id, doctor_id, current_user)
    return {"message": "Patient information sent successfully"}
