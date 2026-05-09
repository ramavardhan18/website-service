from fastapi import APIRouter

router = APIRouter(
    prefix="/api/leads",
    tags=["Leads"]
)

@router.get("/")
def get_leads():
    return {"message": "Get all leads"}

@router.post("/")
def create_lead():
    return {"message": "Lead created successfully"}