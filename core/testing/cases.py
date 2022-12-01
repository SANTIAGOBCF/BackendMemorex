from typing import Union

from django.test import TestCase
from faker import Faker

from core.utils import encode_jwt_token, format_url
from user.factories import UserFactory

_fake = Faker()


class ClientBaseTestCase(TestCase):
    """
    Client Base Test Case
    """

    fake = _fake

    @property
    def headers(self):
        """
        Base headers, can be overridden.
        Includes Bearer Authorization.
        """
        payload = {'id': str(self.user.id)}
        token = encode_jwt_token(payload)
        return {'HTTP_AUTHORIZATION': f'Bearer {token}'}

    def add_user(self, **fields):
        return UserFactory(_resolver='save')

    def _http_method(
        self,
        method: str,
        headers: Union[dict, None] = None,
        input_schema: Union[dict, None] = None,
        url: Union[str, None] = None,
    ):
        if not url:
            url = format_url(self.router, self.url)

        if not input_schema:
            input_schema = {}

        http_method = getattr(self.client, method)
        if headers:
            return http_method(url, input_schema, "application/json", **headers)

        return http_method(url, input_schema, "application/json")

    def get(
        self,
        input_schema: Union[dict, None] = None,
        url: Union[str, None] = None,
        headers: Union[dict, None] = None,
    ):
        return self._http_method(
            method="get",
            headers=headers,
            input_schema=input_schema,
            url=url,
        )

    def patch(
        self,
        input_schema: Union[dict, None] = None,
        url: Union[str, None] = None,
        headers: Union[dict, None] = None,
    ):
        return self._http_method(
            method="patch",
            headers=headers,
            input_schema=input_schema,
            url=url,
        )

    def post(
        self,
        input_schema: Union[dict, None] = None,
        url: Union[str, None] = None,
        headers: Union[dict, None] = None,
    ):
        return self._http_method(
            method="post",
            headers=headers,
            input_schema=input_schema,
            url=url,
        )
