# app/database.py
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

async def init_db():
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",
        modules={"models": ["app.models"]},
    )
    await Tortoise.generate_schemas()

async def close_db():
    await Tortoise.close()

from .models import User

async def get_user_by_username(username: str):
    return await User.filter(username=username).first()
