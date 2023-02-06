from typing import Union

from models.user import UserView, User
from ..functions.generic import Generic


class UserRepository:
    def __init__(self):
        """Product repository class
        """
        self.generic = Generic(self.schema, "users")
    
    def schema(self, document:dict):
        """Return the schema
        """
        return {
            "id": str(document["_id"]),
            "user_name": document["user_name"],
            "full_name": document["full_name"],
            "email": document["email"],
            "password": document["password"],
            "enabled": document["enabled"]
        }
    
    def to_model(self, document:dict):
        """Return the model
        """
        return User(**document)
    
    def to_view(self, document:dict):
        """Return the view
        """
        return UserView(**document)
    
    def search(self, key:str, value:Union[str,any]):
            return self.to_model(self.generic.search(key, value))
        
    def insert(self, document:dict):
        """Insert a document to the collection
        
        Args:
            document (dict): document to be inserted
        """
        return self.to_view(self.generic.insert(document))
    
    def update(self,id:int, document:dict):
        """Update a document in the collection
        
        Args:
            document (dict): document to be updated
        """
        return self.to_view(self.generic.update(id,document))
    
    def update_property(self, id:str, key:str, value:Union[str,any]):
        """Update a property in a document
        
        Args:
            id (str): document id
            key (str): property name
            value (Union[str,any]): property value
        """
        return self.to_view(self.generic.update_field(id, key, value))
    
    def get_all(self):
        """Get all documents from the collection
        
        return: list of documents
        """
        return [self.to_view(document) for document in self.generic.get_all()]
    
    def get_by_id(self, id:str):
        """Get a document by id
        
        Args:
            id (str): document id
        """
        return self.to_view(self.generic.search_by_id(id))
    
    def delete(self, id:str):
        """Delete a document by id
        
        Args:
            id (str): document id
        """
        return self.generic.delete(id)
    