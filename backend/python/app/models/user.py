from typing import Union
from bson import ObjectId
from pydantic import BaseModel


class UserView(BaseModel):
    """User view model"""
    id: Union[str, None]= None
    user_name: str
    full_name: Union[str, None] = None
    email: str
    enabled: bool = True

    
    def to_dict(self):
        """ Return the model as a dictionary
            
            return: dict
        """
        return {
            "id": self.id,
            "user_name": self.user_name,
            "full_name": self.full_name,
            "email": self.email,
            "password": self.password,
            "enabled": self.enabled
        }

class User(BaseModel):
    """User model"""
    password: str