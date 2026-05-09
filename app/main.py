from fastapi import FastAPI

from app.routes import (
    auth_routes,
    lead_routes,
    service_routes
)

from app.config.database import (
    engine,
    Base
)

# Import models
from app.models.user import User
from app.models.lead import Lead
from app.models.service import Service

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="IT Startup Backend",
    version="1.0.0"
)

app.include_router(auth_routes.router)
app.include_router(lead_routes.router)
app.include_router(service_routes.router)


@app.get("/")
def home():
    return {
        "message": "IT Startup Backend Running Successfully"
    }