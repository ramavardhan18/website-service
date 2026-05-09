from fastapi import APIRouter

router = APIRouter(
    prefix="/api/services",
    tags=["Services"]
)

@router.get("/")
def get_services():
    return {"message": "Get all services"}