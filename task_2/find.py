from pymongo.database import Database


def find_all_caats(db: Database) -> list[dict]:
    result = db.cats.find({})
    return list(result)


def find_by_name(db: Database, name: str) -> dict:
    return db.cats.find_one({"name": name})
