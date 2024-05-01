# app/routes/patients.py
from fastapi import APIRouter
from ..schemas import UserBase  # Import the appropriate schema for user data
from ..models import Patient  # Correct import path for Patient model
from app.schemas import PatientCreate

router = APIRouter()

from fastapi import APIRouter

from app.models import Patient
from app.schemas import PatientCreate, Patient as PatientSchema  # Rename Patient to avoid name conflict

router = APIRouter()

@router.post("/", response_model=PatientSchema)  # Adjusted response_model
async def create_patient(patient_data: PatientCreate):
    new_patient = await Patient.create(name=patient_data.name, medical_info=patient_data.medical_info)
    return new_patient


@router.get("/{patient_id}")
async def get_patient(patient_id: int):
    # Logic to retrieve patient information
    patient = await Patient.get_or_none(id=patient_id)
    if not patient:
        return {"error": "Patient not found"}
    return patient
