from pymongo import MongoClient
from pymongo.server_api import ServerApi
from insert import insert_default_data
from find import find_all_caats, find_by_name
from update import update_age_by_name, add_feature_by_name
from delete import delete_by_name, delete_all_cats
from pprint import pprint

client = MongoClient(
    "mongodb://admin:adminpassword@localhost:27017/hw03?authSource=admin",
    server_api=ServerApi("1"),
)

db = client.hw03

insert_default_data(db)

print("Find all cats:")
pprint(find_all_caats(db))

print("Find 'barsik':")
pprint(find_by_name(db, "barsik"))

update_age_by_name(db, "barsik", 10)
add_feature_by_name(db, "Liza", "нявкає в ранці")

delete_by_name(db, "Lama")

print("Find all cats before delete all to compare changes:")
pprint(find_all_caats(db))

delete_all_cats(db)
