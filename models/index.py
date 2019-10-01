from pymongo import MongoClient

mongo_client = get('MONGODB_URI', default='mongodb://localhost:27017')