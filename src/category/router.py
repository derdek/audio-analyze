from fastapi import APIRouter

from src.db import Session
from src.models.category import Category, CategoryPoint

category_router = APIRouter()


@category_router.get("/category")
def read_category():
    session = Session()
    categories = session.query(Category).all()
    result = []
    for category in categories:
        result.append({
            "id": category.id,
            "title": category.title,
            "points": [point.point for point in category.points]
        })
    return result


@category_router.get("/category/{category_id}")
def read_category(category_id: int):
    session = Session()
    category = session.query(Category).get(category_id)
    return {
        "id": category.id,
        "title": category.title,
        "points": [point.point for point in category.points]
    }


@category_router.post("/category")
def create_category(
    title: str,
    points: list[str]
):
    session = Session()
    category = Category(title=title)
    for point in points:
        category.points.append(CategoryPoint(point=point))
    session.add(category)
    session.commit()
    return {
        "id": category.id,
        "title": category.title,
        "points": [point.point for point in category.points]
    }


@category_router.put("/category/{category_id}")
def update_category(
    category_id: int,
    title: str,
    points: list[str]
):
    # update category and points
    session = Session()
    category = session.query(Category).get(category_id)
    category.title = title
    category.points = []
    for point in points:
        category.points.append(CategoryPoint(point=point))
    session.commit()
    return {
        "id": category.id,
        "title": category.title,
        "points": [point.point for point in category.points]
    }


@category_router.delete("/category/{category_id}")
def delete_category(category_id: int):
    session = Session()
    category = session.query(Category).get(category_id)
    session.delete(category)
    session.commit()
    return {"message": "Category deleted successfully"}
