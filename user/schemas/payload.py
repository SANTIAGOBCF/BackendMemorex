from typing import Optional

from ninja import Schema
from pydantic import validator


class PayloadPatchMyAccount(Schema):
    email: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    profile_image: Optional[str]
    password: Optional[str]
    repeat_password: Optional[str]

    @validator("repeat_password")
    def repeat_password_does_not_match(cls, v, values):  # noqa
        if v != values["password"]:
            raise ValueError("Passwords do not match")
        return v


class PayloadPostAddUser(Schema):
    email: str
    first_name: str
    last_name: str
    profile_image: str
    role: str
    password: str
    repeat_password: str

    @validator('repeat_password')
    def repeat_password_does_not_match(cls, v, values):  # noqa
        if v != values['password']:
            raise ValueError('Passwords do not match')
        return v


class PayloadPostLoginUser(Schema):
    email: str
    password: str
