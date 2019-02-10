from smartninja_mongo.connection import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.my_database

collection = db.users

user_id = collection.insert_one({"first_name": "Matej", "last_name": "Ramuta", "year_born": 1987}).inserted_id

user_info = collection.find_one({"_id": user_id})

print(user_info)
