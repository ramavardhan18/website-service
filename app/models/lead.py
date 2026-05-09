from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.sql import func
from app.config.database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    email = Column(String(150))
    phone = Column(String(20))
    company = Column(String(150))
    service_required = Column(String(100))
    project_description = Column(Text)
    budget = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())