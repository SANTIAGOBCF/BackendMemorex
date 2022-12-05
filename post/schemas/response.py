from ninja import ModelSchema

from post.models import Post


class ResponsePost(ModelSchema):
    class Config:
        model = Post
        model_fields = [
            'id',
            'created_at',
            'date',
            'image',
            'source',
            'text',
            'title',
            'updated_at',
        ]
