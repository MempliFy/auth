from uuid import UUID

from fastapi_users import FastAPIUsers
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from app.core.config import settings
from app.db.user_db import get_user_db
from app.models.user import User

# トークンの運搬方法 (HTTPヘッダ "Authorization: Bearer <token>")
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

SECRET_KEY = settings.SECRET_KEY


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET_KEY, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_users = FastAPIUsers[User, UUID](
    get_user_db,
    [auth_backend],
)
