from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.utils.send_email import send_lead_email

from app.config.database import get_db

from app.models.lead import Lead

from app.schemas.lead_schema import (
    LeadCreate
)

router = APIRouter(
    prefix="/api/leads",
    tags=["Leads"]
)


# Create Lead
@router.post("/")
def create_lead(
    request: LeadCreate,
    db: Session = Depends(get_db)
):

    new_lead = Lead(
        full_name=request.full_name,
        email=request.email,
        phone=request.phone,
        company=request.company,
        service_required=request.service_required,
        project_description=request.project_description,
        budget=request.budget
    )

    db.add(new_lead)

    db.commit()

    db.refresh(new_lead)

    send_lead_email(new_lead)

    return {
        "message": "Lead submitted successfully"
    }


# Get All Leads
@router.get("/")
def get_all_leads(
    db: Session = Depends(get_db)
):

    leads = db.query(Lead).all()

    return leads


# Delete Lead
@router.delete("/{lead_id}")
def delete_lead(
    lead_id: int,
    db: Session = Depends(get_db)
):

    lead = db.query(Lead).filter(
        Lead.id == lead_id
    ).first()

    if not lead:

        raise HTTPException(
            status_code=404,
            detail="Lead not found"
        )

    db.delete(lead)

    db.commit()

    return {
        "message": "Lead deleted successfully"
    }