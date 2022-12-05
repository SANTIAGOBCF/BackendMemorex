from politician.constants import Endpoints

from .cases import PoliticianTestCase


class GetPolitician(PoliticianTestCase):
    url = Endpoints.GET_POLITICIAN

    def setUp(self):
        self.user = self.add_user()

    def test_get_politician_returns_200(self):
        politician = self.add_politician()
        self.url = self.url.format(id=politician.id)

        response = self.get()
        self.assertEqual(response.status_code, 200)

    def test_get_politician_returns_404_if_politician_does_NOT_exist(self):
        self.url = self.url.format(id=self.user.id)

        response = self.get()
        self.assertEqual(response.status_code, 404)


class GetPoliticianList(PoliticianTestCase):
    url = Endpoints.GET_POLITICIAN_LIST

    def setUp(self):
        self.user = self.add_user()


class PatchPolitician(PoliticianTestCase):
    url = Endpoints.PATCH_POLITICIAN

    def setUp(self):
        self.user = self.add_user()

        self.input_schema = {
            'description': self.fake.text(),
            'name': self.fake.name(),
            'organization': self.fake.name(),
            'profile_image': self.fake.image_url(),
            'reference': self.fake.image_url(),
        }

    def test_patch_politician_returns_200(self):
        politician = self.add_politician()
        self.url = self.url.format(id=politician.id)

        response = self.patch(input_schema=self.input_schema, headers=self.headers)
        self.assertEqual(response.status_code, 200)


class PostAddPolitician(PoliticianTestCase):
    url = Endpoints.POST_ADD_POLICIAN

    def setUp(self):
        self.user = self.add_user()
        self.input_schema = {
            'description': self.fake.text(),
            'name': self.fake.name(),
            'organization': self.fake.name(),
            'profile_image': self.fake.image_url(),
            'reference': self.fake.image_url(),
        }

    def test_add_politician_returns_201(self):
        response = self.post(input_schema=self.input_schema, headers=self.headers)
        self.assertEqual(response.status_code, 201)
