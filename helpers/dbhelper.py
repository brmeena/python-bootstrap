import sys
sys.path.append("../")
from Config import config
import pymongo
from bson.objectid import ObjectId
def getMongoDatabase():
    mconn=pymongo.MongoClient(config.getMongoConnectionString())
    return mconn.sampledb

def fromStringToObjectId(strId):
    return ObjectId(strId)