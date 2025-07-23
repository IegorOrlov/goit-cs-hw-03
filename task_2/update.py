from pymongo.database import Database
from error_handler import mongo_error_handler


@mongo_error_handler
def update_age_by_name(db: Database, name: str, age: int) -> None:
    db.cats.update_one({"name": name}, {"$set": {"age": age}})


@mongo_error_handler
def add_feature_by_name(db: Database, name: str, feature: str) -> None:
    db.cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
