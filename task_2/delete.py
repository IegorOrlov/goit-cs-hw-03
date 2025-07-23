from pymongo.database import Database
from error_handler import mongo_error_handler


@mongo_error_handler
def delete_by_name(db: Database, name: str) -> None:
    db.cats.delete_one({"name": name})


@mongo_error_handler
def delete_all_cats(db: Database) -> None:
    db.cats.delete_many({})
