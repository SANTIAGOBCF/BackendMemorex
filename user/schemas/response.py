from ninja import ModelSchema

from user.models import User


class ResponseUser(ModelSchema):
    class Config:
        model = User
        model_fields = [
            'id',
            'created_at',
            'email',
            'first_name',
            'last_name',
            'last_login',
            'profile_image',
            'role',
            'updated_at',
        ]
