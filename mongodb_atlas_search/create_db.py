# # Insert items
import pymongo

def db_creation(collection):
    item_1 = {
    "title" : "fitness",
    "message" : "I am going to run, begin",
    }

    item_2 = {
    "title" : "exercise",
    "message" : "they GO to running, beginning",
    }

    item_3 = {
    "title" : "todo",
    "message" : "go go power rangers, begins",
    }

    item_4 = {
    "title" : "exercise",
    "message" : "they go to running, started",
    }

    item_5 = {
    "title" : "making",
    "message" : "went for my beginning",
    }
    item_6 = {
    "title" : "trying",
    "message" : "I am in the 10th place",
    }
    item_7 = {
    "title" : "place",
    "message" : "Again the tenth place",
    }
    collection.insert_many([item_1,item_2,item_3,item_4, item_5,item_6, item_7])