# app/services/user_service.py
from passlib.context import CryptContext
from ..models import User
from ..schemas import UserCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def authenticate_user(username: str, password: str):
    user = await User.get_or_none(username=username)
    if not user or not verify_password(password, user.password):
        return None
    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

async def create_user(user_data: UserCreate):
    hashed_password = get_password_hash(user_data.password)
    user = await User.create(username=user_data.username, password=hashed_password, role=user_data.role)
    return user
