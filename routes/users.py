from __future__ import annotations

from fastapi import APIRouter, Depends

from models.user import User
from schemas.user import UserResponse
from services.auth_service import get_current_user

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)) -> User:
    return current_user
