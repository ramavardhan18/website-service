from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import get_db
from app.models.user import User

from app.schemas.auth_schema import (
    RegisterSchema,
    LoginSchema
)

from app.utils.password import (
    hash_password,
    verify_password
)

from app.utils.jwt_handler import (
    create_access_token
)

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    request: RegisterSchema,
    db: Session = Depends(get_db)
):

    existing_user = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = User(
        username=request.username,
        email=request.email,
        password=hash_password(request.password)
    )

    db.add(new_user)

    db.commit()

    db.refresh(new_user)

    return {
        "message": "Admin registered successfully"
    }


@router.post("/login")
def login(
    request: LoginSchema,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email"
        )

    if not verify_password(
        request.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    access_token = create_access_token(
        data={
            "sub": user.email
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }