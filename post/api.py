from ninja import Router

from user.bearers import AuthBearer

from .constants import Endpoints
from .models import Post
from .schemas.payload import PayloadPostAddPost
from .schemas.response import ResponsePost

router = Router()


@router.post(
    Endpoints.POST_ADD_POST,
    auth=AuthBearer(),
    response={201: ResponsePost},
)
def add_post(request, data: PayloadPostAddPost):
    """
    Create a new post.
    """
    post_data = data.dict()
    post_data['author_id'] = request.user.id

    return Post.objects.create(**post_data)
