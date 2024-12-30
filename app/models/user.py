import uuid

from fastapi_users.db import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Boolean, Column
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    is_premium = Column(Boolean, default=False)
