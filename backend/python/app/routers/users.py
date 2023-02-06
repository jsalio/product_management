from fastapi import APIRouter, Depends, HTTPException, status
from models.user import UserView
from db.schema.user_repository import UserRepository 

router = APIRouter(prefix="/api/user", tags=["Users"])

@router.get("/", response_model=list[UserView], status_code=status.HTTP_200_OK)
async def get_all():
    try:
        repo = UserRepository()
        return repo.get_all()
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail=str(e))
    
@router.get("/{id}", response_model=UserView, status_code=status.HTTP_200_OK)
async def get_by_id(id:str):
    try:
        repo = UserRepository()
        return repo.get_by_id(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_302_FOUND, detail=str(e))

@router.post("/" , response_model=UserView, status_code=status.HTTP_201_CREATED)
async def insert(user:UserView):
    """Insert a new user into repository
    
    Args:
        user (UserView): user to be inserted
    
    return: UserView
    """
    try:
        repo = UserRepository()
        return repo.insert(user.dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    
@router.put("/{id}", response_model=UserView, status_code=status.HTTP_202_ACCEPTED)
async def update(id:str, user:UserView):
    """Update a user
    
    Args:
        id (str): id of the user
        user (UserView): user to be updated
    
    return: UserView
    """
    try:
        repo = UserRepository()
        return repo.update(id,user.dict())
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail=str(e))
    
@router.put("/{id}/{key}/{value}", response_model=UserView, status_code=status.HTTP_202_ACCEPTED)
async def update_property(id:str, key:str, value:str):
    """Update a property in a user
    
    Args:
        id (str): id of the user
        key (str): property name
        value (str): property value
    
    return: UserView
    """
    try:
        repo = UserRepository()
        return repo.update_property(id,key,value)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail=str(e))
    
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id:str):
    """Delete a user
    
    Args:
        id (str): id of the user
    
    return: UserView
    """
    try:
        repo = UserRepository()
        repo.delete(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED, detail=str(e))