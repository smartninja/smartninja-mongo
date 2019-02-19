# SmartNinja Mongo

A simple **wrapper** for MongoDB (`pymongo`) and TinyDB (`tinymongo`). It also provides a lightweight **object-document mapper** (ODM).

Use it if you don't want to (or can't) install MongoDB locally.

## Installation

Install the package via pip:

	pip install smartninja-mongo

Or add it in your `requirements.txt` and run `pip install -r requirements.txt`.

### Dependencies

SmartNinja Mongo automatically installs the following dependencies:

- `tinymongo`
- `pymongo`
- `tinydb`
- `tinydb_serialization` (used to easily convert datetime objects)

## How it works

You write your code as you would using the `pymongo` package. Except that you get the `MongoClient` class from the `smartninja_mongo` library (see examples below).

SmartNinja Mongo **automatically** figures out whether you're the program is running on **localhost** or on a **production** server.

If it's on **localhost**, TinyDB will be used instead of MongoDB via the `tinymongo` package (except if you set the `CUSTOM_MONGO_SERVER` env var).

If the app runs on **Heroku** or on **Azure**, the `smartninja_mongo` package automatically recognizes this and returns the `pymongo` client class instead of the one from `tinymongo`.

If your program runs in **some other production environment**, just set the `CUSTOM_MONGO_SERVER` env var (add any value to it that comes back as `True`, like for example `"1"`) and `pymongo` client will be used.

## Usage

SmartNinja Mongo's only task is to get you the right Mongo client:

```python
from smartninja_mongo.connection import MongoClient

client = MongoClient('mongodb://ds012345.mlab.com:56789/')
```

If your Python program runs on Heroku (for example), you'll get back a `MongoClient` from the `pymongo` library which has a connection to the production MongoDB database (in this case the mLab's Mongo database).

But if your app runs on localhost, a TinyDB instance will be created (you'll see a `localhost.db` folder created, put it in `.gitignore`).

Even if TinyDB is used on localhost instead of the MongoDB, you can write your code in the MongoDB way (or `pymongo` way).

See the following examples:

```python
db = client.my_database

collection = db.users

user_id = collection.insert_one({"first_name": "Matej", "last_name": "Ramuta", "year_born": 1987, "created": datetime.datetime.now()}).inserted_id

from smartninja_mongo.bson import ObjectId
user_info = collection.find_one({"_id": ObjectId(user_id)})

print(user_info)
```

As you can see, the `bson.ObjectId` is needed when searching by ID.

### More usage examples

For more usage examples see PyMongo docs: [https://api.mongodb.com/python/current/](https://api.mongodb.com/python/current/).

### Beware

There might be some incompatibilities between TinyMongo and PyMongo. Make sure to also check the [TinyMongo docs](https://tinydb.readthedocs.io/en/latest/index.html) to identify the problem if weird behavior occurs.

### ODM

MongoDB accepts data as dictionaries and also returns data as dicts. If you'd like to use model classes in your project, you can use a base model from the SmartNinja Mongo library:

```python
from smartninja_mongo.odm import Model


class User(Model):
    def __init__(self, first_name, **kwargs):
        self.first_name = first_name

        super().__init__(**kwargs)
```

Make sure to add `**kwargs` as a parameter and call `super()` at the end of the `__init__` method.

Alternatively you can skip `__init__` completely

```python
class User(Model):
	pass
```

#### The benefit of using SmartNinja Mongo ODM `Model`

The main benefit is that you get a method called: `convert_dict_to_object()`:

```python
user_info = collection.find_one({"_id": ObjectId(user_id)})

user_obj = User.convert_dict_to_object(data_dict=user_info)

print(user_obj.first_name)
```

This `Model` class provides a very lightweight and simple **object-document mapping** (ODM).

## Contributions

Contributions via pull requests are warmly welcome!

### TODO

- tests
- CI