# main.py
from fastapi import FastAPI
from app.database import init_db, close_db  
from app.routes import users, doctors, patients 

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(doctors.router, prefix="/doctors", tags=["doctors"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])

@app.on_event("startup")
async def startup_db_client():
    await init_db()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_db()
