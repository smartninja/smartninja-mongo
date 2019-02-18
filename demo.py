import datetime

from smartninja_mongo.bson import ObjectId
from smartninja_mongo.connection import MongoClient
from smartninja_mongo.odm import Model

client = MongoClient('mongodb://localhost:27017/')

db = client.my_database

collection = db.users

user_id = collection.insert_one({"first_name": "Matej", "last_name": "Ramuta", "year_born": 1987,
                                 "created": datetime.datetime.now()}).inserted_id

user_info = collection.find_one({"_id": user_id})

print(user_info)

try:
    print(user_info.first_name)
except Exception as e:
    print("Error because user_info is a dict, not an object")


class User(Model):
    def __init__(self, first_name, **kwargs):
        self.first_name = first_name

        super().__init__(**kwargs)


print("Let's convert user_dict into an object")
user_obj = User.convert_dict_to_object(data_dict=user_info)
print(user_obj.first_name)

print("-----------")

user_id_bson = ObjectId(user_id)
print(user_id_bson)
print(type(user_id_bson))
user_info = collection.find_one({"_id": ObjectId(user_id)})

print(user_info)

collection.delete_many({})
