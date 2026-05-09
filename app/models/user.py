from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.sql import func
from app.config.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)

    email = Column(String(150), unique=True, nullable=False)

    password = Column(String(255), nullable=False)

    role = Column(String(50), default="admin")

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )