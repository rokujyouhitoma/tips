from functools import wraps
import sqlite3 as sqlite

from fastapi import FastAPI, HTTPException
from pydantic import BaseSettings
from pydantic import BaseModel

from app import docclass

classifier = docclass.fisherclassifier(docclass.getwords)


classifier.setdb("/tmp/classifier.db")
with sqlite.connect(classifier.db_uri) as connection:
    classifier.con = connection
    classifier.init_db()


def db_connection_decorator(classifier):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            with sqlite.connect(classifier.db_uri) as connection:
                classifier.con = connection
                result = func(*args, **kwargs)
            classifier.con = None
            return result

        import inspect

        wrapper.__signature__ = inspect.Signature(
            parameters=[
                *inspect.signature(func).parameters.values(),
                *filter(
                    lambda p: p.kind
                    not in (
                        inspect.Parameter.VAR_POSITIONAL,
                        inspect.Parameter.VAR_KEYWORD,
                    ),
                    inspect.signature(wrapper).parameters.values(),
                ),
            ],
            return_annotation=inspect.signature(func).return_annotation,
        )
        return inner

    return wrapper


class Category(BaseModel):
    category: str
    count: int


class Feature(BaseModel):
    feature: str
    category: str
    count: int


class Document(BaseModel):
    document: str
    category: str


class ClassificationResult(BaseModel):
    category: str


class Settings(BaseSettings):
    root_path: str = ""


settings = Settings()

app = FastAPI(root_path=settings.root_path)


@app.get("/")
def read_root():
    return {}


@app.post("/items/flush/")
@db_connection_decorator(classifier)
def flush_all_data():
    """
    推論モデルを破棄する。
    """
    classifier.flush_database()
    return "ok"


@app.get("/items/features/")
@db_connection_decorator(classifier)
def read_items_features() -> list[Feature]:
    """
    推論モデルの特徴量
    """
    return [
        Feature(feature=v[0], category=v[1], count=v[2]) for v in classifier.fc_all()
    ]


@app.get("/items/categories/")
@db_connection_decorator(classifier)
def read_items_categories() -> list[Category]:
    """
    推論モデルのカテゴリー
    """
    return [Category(category=v[0], count=v[1]) for v in classifier.cc_all()]


@app.post("/items/")
@db_connection_decorator(classifier)
def create_items(items: list[Document]):
    """
    学習する。
    """
    result = [{"doc": item.document, "category": item.category} for item in items]

    for item in items:
        classifier.train(item.document, item.category)

    return result


@app.post("/items/classify/")
@db_connection_decorator(classifier)
def classify(text: str) -> ClassificationResult:
    """
    推論する。
    """
    category = classifier.classify(text)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return ClassificationResult(category=category)
