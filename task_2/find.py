from pymongo.database import Database
from error_handler import mongo_error_handler


@mongo_error_handler
def find_all_caats(db: Database) -> list[dict]:
    result = db.cats.find({})
    return list(result)


@mongo_error_handler
def find_by_name(db: Database, name: str) -> dict:
    return db.cats.find_one({"name": name})
