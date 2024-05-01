# app/services/doctor_service.py
from fastapi import HTTPException
from ..models import Doctor, Patient

async def send_patient_info(patient_id: int, doctor_id: int, current_user):
    doctor = await Doctor.get_or_none(id=doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    
    patient = await Patient.get_or_none(id=patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    await doctor.patients.add(patient)
