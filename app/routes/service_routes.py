from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.config.database import get_db

from app.models.service import Service

from app.schemas.service_schema import (
    ServiceCreate
)

router = APIRouter(
    prefix="/api/services",
    tags=["Services"]
)


# Create Service
@router.post("/")
def create_service(
    request: ServiceCreate,
    db: Session = Depends(get_db)
):

    new_service = Service(
        title=request.title,
        description=request.description
    )

    db.add(new_service)

    db.commit()

    db.refresh(new_service)

    return {
        "message": "Service created successfully"
    }


# Get All Services
@router.get("/")
def get_all_services(
    db: Session = Depends(get_db)
):

    services = db.query(Service).all()

    return services


# Update Service
@router.put("/{service_id}")
def update_service(
    service_id: int,
    request: ServiceCreate,
    db: Session = Depends(get_db)
):

    service = db.query(Service).filter(
        Service.id == service_id
    ).first()

    if not service:

        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    service.title = request.title
    service.description = request.description

    db.commit()

    return {
        "message": "Service updated successfully"
    }


# Delete Service
@router.delete("/{service_id}")
def delete_service(
    service_id: int,
    db: Session = Depends(get_db)
):

    service = db.query(Service).filter(
        Service.id == service_id
    ).first()

    if not service:

        raise HTTPException(
            status_code=404,
            detail="Service not found"
        )

    db.delete(service)

    db.commit()

    return {
        "message": "Service deleted successfully"
    }