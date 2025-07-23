from pymongo.errors import PyMongoError
from functools import wraps
from typing import Callable, TypeVar, Any, Optional

F = TypeVar("F", bound=Callable[..., Any])

def mongo_error_handler(func: F) -> F:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Optional[Any]:
        try:
            return func(*args, **kwargs)
        except PyMongoError as e:
            print(f"[MongoError] {func.__name__}: {e}")
            return None
    return wrapper  # type: ignore