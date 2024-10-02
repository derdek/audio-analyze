from fastapi import APIRouter

from src.call.router import call_router
from src.category.router import category_router

main_router = APIRouter()
main_router.include_router(category_router)
main_router.include_router(call_router)
