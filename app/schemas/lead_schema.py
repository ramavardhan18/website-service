from pydantic import BaseModel, EmailStr


class LeadCreate(BaseModel):

    full_name: str

    email: EmailStr

    phone: str

    company: str

    service_required: str

    project_description: str

    budget: str