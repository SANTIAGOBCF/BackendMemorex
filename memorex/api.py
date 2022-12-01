from ninja import NinjaAPI

from politician.api import router as politician_router
from user.api import router as user_router

from .constants import Routers

api = NinjaAPI()

# Django Ninja API Routers
api.add_router(Routers.POLITICIAN, politician_router, tags=["Politician"])
api.add_router(Routers.USER, user_router, tags=["User"])
