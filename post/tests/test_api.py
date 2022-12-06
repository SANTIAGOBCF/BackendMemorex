from post.constants import Endpoints

from .cases import PostTestCase


class PostAddPost(PostTestCase):
    url = Endpoints.POST_ADD_POST

    def setUp(self):
        self.user = self.add_user()
        self.politician = self.add_politician()
        self.input_schema = {
            'politician_id': self.politician.id,
            'date': self.fake.date(),
            'image': self.fake.image_url(),
            'source': self.fake.image_url(),
            'text': self.fake.text(),
            'title': self.fake.name(),
        }

    def test_add_politician_returns_201(self):
        response = self.post(input_schema=self.input_schema, headers=self.headers)
        self.assertEqual(response.status_code, 201)
