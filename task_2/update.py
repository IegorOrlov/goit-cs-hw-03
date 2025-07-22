from pymongo.database import Database


def update_age_by_name(db: Database, name: str, age: int) -> None:
    db.cats.update_one({"name": name}, {"$set": {"age": age}})


def add_feature_by_name(db: Database, name: str, feature: str) -> None:
    db.cats.update_one({"name": name}, {"$addToSet": {"features": feature}})
