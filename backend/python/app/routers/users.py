from fastapi import APIRouter, Depends, HTTPException, status
from ..db.schema.user_repository import UserRepository 

router = APIRouter("api/users", tags=["users"])

@router.get("/")
async def get_all():
    try:
        repo = UserRepository()
        return repo.get_all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))