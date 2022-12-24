from django.shortcuts import get_object_or_404
from ninja import Query, Router

from core.filters import FilterPagination
from core.utils import get_paginated_queryset
from user.bearers import AuthBearer

from .constants import Endpoints
from .models import Post
from .schemas.payload import PayloadPostAddPost
from .schemas.response import ResponseGetPostList, ResponsePostAddPost

router = Router()


@router.delete(
    Endpoints.DELETE_POST,
    response=str,
)
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return f'Post #{id} was deleted'


@router.post(
    Endpoints.POST_ADD_POST,
    auth=AuthBearer(),
    response={201: ResponsePostAddPost},
)
def add_post(request, data: PayloadPostAddPost):
    """
    Create a new post.
    """
    post_data = data.dict()
    post_data['author_id'] = request.user.id

    return Post.objects.create(**post_data)


@router.get(
    Endpoints.GET_POST_LIST,
    response=ResponseGetPostList,
)
def get_post_list(request, data: FilterPagination = Query(...)):
    queryset = Post.objects.all()
    count = queryset.count()
    queryset = get_paginated_queryset(queryset, data.limit, data.offset)
    return {'posts': list(queryset), 'count': count}
