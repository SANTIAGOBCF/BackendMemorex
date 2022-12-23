from ninja import ModelSchema

from post.models import Post


class SchemaPost(ModelSchema):
    class Config:
        model = Post
        model_fields = '__all__'
