# app/routes/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from ..authentication import create_access_token
from ..database import init_db, close_db
from ..schemas import Token
from ..services.user_service import authenticate_user
from app.models import User
from app.schemas import UserCreate

router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/logout")
async def logout():
    # Logout logic
    return {"message": "Logout successful"}

# app/routes/users.py



@router.post("/register")
async def register_user(user_data: UserCreate):
    # Check if the user already exists
    existing_user = await User.get_or_none(username=user_data.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    # Create the user with the provided data
    user = await User.create(username=user_data.username, password=user_data.password, role=user_data.role)
    return user
