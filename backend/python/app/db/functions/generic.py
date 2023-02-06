
from bson.objectid import ObjectId
from ..client import db_client
from typing import Union
from ...models.errors.invalid_exceptions import InvalidArgException


class Generic :
    def __init__(self, schema:dict, collection:str):
        """Generic class for database operations

        Args:
            schema (dict): model schema of the collection
            collection (str): name of the collection
        """
        self.schema = schema
        self.collection = collection
        
    def schema(self):
        "Return the schema"
        return self.schema
    
    def collection(self):
        "Return the collection name"
        return self.collection
    
    def insert(self, document:dict):
        """Insert a document to the collection
        
        Args:
            document (dict): document to be inserted
        """
        try:
            identificator = db_client[self.collection].insert_one(document).inserted_id
            return self.schema(db_client[self.collection].find_one({"_id":ObjectId(identificator)}))
        except Exception as e:
            return None
    
    def get_all(self):
        """Get all documents from the collection
        
        return: list of documents
        """
        try:
            documents = db_client[self.collection].find()
            return [self.schema(document) for document in documents]
        except Exception as e:
            return None
        
    def search(self, key:str, value:Union[str,any]):
        """Search for a document by key and value

        Args:
            key (str): name of the key
            value (Union[str,any]): value of the key

        Returns:
            _type_: document
        """
        try:
            document = self.schema(db_client[self.collection].find_one({key:value}))
            return document 
        except Exception as e:
            return None
        
    def search_by_id(self, id:str):
        """Search for a document by id"""
        try:
            return self.search("_id", ObjectId(id))
        except Exception as e:
            return None
        
    def update(self, id:str, document:dict):
        """ find and update a document by id

        Args:
            id (str): id of the document
            document (dict): document to be updated

        Raises:
            InvalidArgException:  if the document not exist

        Returns:
            _type_: bool
        """
        try:
            if not self.search_by_id(id):
                raise InvalidArgException("Document not exist")
            updated = db_client[self.collection].find_one_and_replace({"_id":ObjectId(id)},document)
            if updated:
                return True
            return False
        except Exception as e:
            return False
    
    def update_field(self, id:str, key:str, value:Union[str,any]):
        """update a field of a document by id

        Args:
            id (str): id of the document
            key (str): name of the key
            value (Union[str,any]): value of the key to be updated

        Raises:
            InvalidArgException: if the document not exist

        Returns:
            _type_: bool
        """
        try:
            if not self.search_by_id(id):
                raise InvalidArgException("Document not exist")
            updated = db_client[self.collection].find_one_and_update({"_id":ObjectId(id)}, {"$set":{key:value}})
            if updated:
                return True
            return False
        except Exception as e:
            return False
        
    def delete(self, id:str):
        """Delete a document by id

        Args:
            id (str): id of the document

        Returns:
            _type_: bool
        """
        try:
            document = self.search_by_id(id)
            if not document:
                return False
            deleted = db_client[self.collection].find_one_and_delete({"_id":ObjectId(document["id"])})
            if not deleted:
                return False
            return True
        except Exception as e:
            return False