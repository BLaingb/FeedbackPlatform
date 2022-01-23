from fastapi import APIRouter

from app.api.api_v1.endpoints import utils
from app.modules.auth.api.v1.endpoints import login, users, roles
from app.modules.chapters.api.v1.endpoints import chapters

api_router = APIRouter()
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])

# Auth
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(roles.router, prefix="/roles", tags=["roles"])

# Chapters
api_router.include_router(chapters.router, prefix="/chapters", tags=["chapters"])
