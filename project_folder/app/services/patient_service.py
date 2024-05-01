# app/services/patient_service.py
from ..models import Patient

async def create_patient(patient_data: dict):
    patient = await Patient.create(**patient_data)
    return patient

async def get_patient(patient_id: int):
    patient = await Patient.get_or_none(id=patient_id)
    return patient
