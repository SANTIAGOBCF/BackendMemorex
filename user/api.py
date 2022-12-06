from django.db import transaction
from django.shortcuts import get_object_or_404
from ninja import Router
from ninja.errors import HttpError

from core.utils import get_jwt_token

from .bearers import AuthBearer
from .constants import Endpoints
from .models import User
from .schemas.payload import (PayloadPatchMyAccount, PayloadPostAddUser,
                              PayloadPostLoginUser)
from .schemas.response import ResponseUser

router = Router()


@router.get(
    Endpoints.GET_ME,
    auth=AuthBearer(),
    response=ResponseUser,
)
def get_my_account(request):
    """
    Get my user profile.
    """
    return request.user


@router.patch(
    Endpoints.PATCH_MY_ACCOUNT,
    auth=AuthBearer(),
    response=ResponseUser,
)
def patch_my_account(request, data: PayloadPatchMyAccount):
    """
    Edit my user account.
    """
    user = request.user
    patch_data = data.dict(exclude_unset=True)
    if data.repeat_password:
        patch_data.pop('repeat_password', None)

    for key, value in patch_data.items():
        setattr(user, key, value)

    return user


@transaction.atomic
@router.post(
    Endpoints.POST_ADD_USER,
    auth=None,
    response={201: ResponseUser},
)
def register_user(request, data: PayloadPostAddUser):
    """
    Registration of a user account.
    """
    user_data = data.dict(
        include={
            'email',
            'first_name',
            'last_name',
            'password',
            'profile_image',
            'role',
        }
    )

    return User.objects.create_user(**user_data)


@router.post(Endpoints.POST_LOGIN, auth=None, response=str)
def login(request, data: PayloadPostLoginUser):
    """
    Returns the access token if correct credentials
    """
    error_msg = "Your email and/or password are wrong."
    user = get_object_or_404(User, email=data.email)
    if user.check_password(data.password):
        return get_jwt_token(user)

    raise HttpError(403, error_msg)
