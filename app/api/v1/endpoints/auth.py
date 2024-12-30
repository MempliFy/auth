from fastapi import APIRouter

from app.core.security import auth_backend, fastapi_users
from app.schemas.user import UserCreate, UserRead

router = APIRouter()

# JWT認証ルーターを取得
auth_router = fastapi_users.get_auth_router(auth_backend)
register_router = fastapi_users.get_register_router(user_schema=UserRead, user_create_schema=UserCreate)


router.include_router(auth_router, prefix="/jwt", tags=["auth"])
router.include_router(register_router, prefix="", tags=["auth"])
