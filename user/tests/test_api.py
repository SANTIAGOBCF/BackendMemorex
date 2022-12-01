from user.constants import Endpoints

from .cases import UserTestCase


class PatchMyAccount(UserTestCase):
    url = Endpoints.PATCH_MY_ACCOUNT

    def setUp(self):
        self.user = self.add_user()
        self.password = self.fake.password()
        self.input_schema = {
            'email': self.fake.email(),
            'first_name': self.fake.name(),
            'last_name': self.fake.name(),
            'password': self.password,
            'repeat_password': self.password,
            'profile_image': self.fake.image_url(),
        }

    def test_patch_my_account_returns_200(self):
        response = self.patch(input_schema=self.input_schema, headers=self.headers)
        self.assertEqual(response.status_code, 200)


class PostAddUser(UserTestCase):
    url = Endpoints.POST_ADD_USER

    def setUp(self):
        self.password = self.fake.password()
        self.input_schema = {
            'email': self.fake.email(),
            'first_name': self.fake.name(),
            'last_name': self.fake.name(),
            'password': self.password,
            'repeat_password': self.password,
            'profile_image': self.fake.image_url(),
            'role': self.fake.name(),
        }

    def test_add_user_returns_201(self):
        response = self.post(input_schema=self.input_schema)
        self.assertEqual(response.status_code, 201)


class PostLogin(UserTestCase):
    url = Endpoints.POST_LOGIN

    def setUp(self):
        self.password = self.fake.password()
        self.user = self.add_user()
        self.user.set_password(self.password)
        self.user.save()

    def test_login_returns_200(self):
        input_schema = {
            "email": self.user.email,
            "password": self.password,
        }

        response = self.post(input_schema=input_schema)
        self.assertEqual(response.status_code, 200)

    def test_login_returns_403_if_not_valid_input(self):
        input_schema = {
            "email": self.user.email,
            "password": f'wrong_{self.password}',
        }

        response = self.post(input_schema=input_schema)
        self.assertEqual(response.status_code, 403)

    def test_login_returns_404_if_not_valid_email(self):
        input_schema = {
            "email": f'wrong_{self.user.email}',
            "password": self.password,
        }

        response = self.post(input_schema=input_schema)
        self.assertEqual(response.status_code, 404)
