from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    TIMESTAMP
)

from sqlalchemy.sql import func

from app.config.database import Base


class Service(Base):

    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(150))

    description = Column(Text)

    icon = Column(String(100))

    created_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )