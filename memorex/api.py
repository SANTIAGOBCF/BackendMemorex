from ninja import NinjaAPI

from politician.api import router as politician_router
from post.api import router as post_router
from user.api import router as user_router
from image_uploader.api import router as image_router

from .constants import Routers

api = NinjaAPI()

# Django Ninja API Routers
api.add_router(Routers.POLITICIAN, politician_router, tags=["Politician"])
api.add_router(Routers.POST, post_router, tags=["Post"])
api.add_router(Routers.USER, user_router, tags=["User"])
api.add_router(Routers.IMAGEUPLOAD, image_router, tags=["Image"])
