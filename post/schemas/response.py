from typing import List

from ninja import Schema

from .common import SchemaPost


class ResponseGetPostList(Schema):
    posts: List[SchemaPost]
    count: int


class ResponsePostAddPost(SchemaPost):
    pass
