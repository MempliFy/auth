from fastapi import APIRouter

from app.core.security import fastapi_users
from app.schemas.user import UserRead, UserUpdate

router = APIRouter()

users_router = fastapi_users.get_users_router(user_schema=UserRead, user_update_schema=UserUpdate)

router.include_router(users_router, prefix="", tags=["users"])
