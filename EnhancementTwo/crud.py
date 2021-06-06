#CRUD Module 4
#Shaun Richardson
#SNHU CS-499-T5477

import os
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
import pprint

class BidSystem(object):
    """ CRUD operations for items collection in MongoDB """
 #connection to the Bid database in MongoDB takes a username/password.
 #The user is already given access within the database.    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/Bid' % (username, password))
        self.database = self.client['Bid']
       

 # Create method to add new items to the Bid database.
    def create(self, data):
        if data is not None:
            data_create = self.database.items.insert(data)  # data should be dictionary
            return data_create
        else:
            raise Exception("Nothing to save, because data parameter is incorrectly formatted")

# Read method to find one or all items within the Bid database.
    def read(self,data):
        if data is not None:    
            data_read = self.database.items.find_one(data,)
            return data_read
        else:
            raise Exception("Nothing to read because data parameter is incorrectly formatted")
    def readAll(self, data):    
        data_read = self.database.items.find(data,{"_id":False})   
        return data_read
    
# Update method to update items within the Bid database.
    
    def update(self, query, data):
        if data is not None:    
            data_update = self.database.items.update_one(query, data)
            return data_update
        else:
            raise Exception("Nothing to update because data parameter is incorrectly formatted")
          
 # Delete method to remove items from the Bid database.
    
    def delete(self,data):
        if data is not None:    
            data_delete = self.database.items.delete_one(data)
            return data_delete
        else:
            raise Exception("Nothing to delete because data parameter is incorrectly formatted")
