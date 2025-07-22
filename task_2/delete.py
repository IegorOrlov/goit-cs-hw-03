from pymongo.database import Database


def delete_by_name(db: Database, name: str) -> None:
    db.cats.delete_one({"name": name})


def delete_all_cats(db: Database) -> None:
    db.cats.delete_many({})
