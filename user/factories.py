from faketory.factory import Faketory
from faketory.gens import Fake

from .models import User


class UserFactory(Faketory):
    email = Fake('unique.ascii_free_email')
    first_name = Fake('name')
    last_name = Fake('name')
    profile_image = Fake('image_url')
    role = Fake('name')

    class Meta:
        model = User
