#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 20:42:56 2024

@author: derekkwasniew_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        # Use following command to retreive Shell variable values for connecting to MongoSH
        # printenv | grep -1 mongo
        #
        # USER = 'aacuser'
        # PASS = '1234'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31283 # Use above command to get port for database
        DB = 'aac'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        print("Connection Successful")

# Create Method
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert_one(data)  # data should be dictionary
            return insert.acknowledged  # Return if the insert was written or not
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Read Method
# Returns a list of all the documents that match the query
    def read(self, data):
        query_List = []
        if data is not None:
            for animal in self.collection.find(data):
                query_List.append(animal)
        else:
            for animal in self.collection.find():
                query_List.append(animal)
        return query_List
            
# Update Method
    def update(self, data, dataToChange):
        if data is not None and dataToChange is not None:
            result = self.collection.update_many(data, dataToChange)
            print("Documents Updated: {}".format(result.modified_count))
        else:
            raise Exception("Data missing for update")
            
# Delete Method
    def delete(self, data):
        if data is not None:
            delete = self.collection.delete_many(data)
            print("Documents Deleted: {}".format(delete.deleted_count))
        else:
            raise Exception("Data missing for delete")