from faketory.factory import Faketory
from faketory.gens import Fake, FaketoryGen

from politician.tests.factories import FactoryPolitician
from post.models import Post
from user.tests.factories import FactoryUser


class PostFactory(Faketory):
    author = FaketoryGen(
        FactoryUser,
        _resolver="save",
    )
    politician = FaketoryGen(
        FactoryPolitician,
        _resolver="save",
    )

    date = Fake('date')
    image = Fake('image_url')
    source = Fake('image_url')
    text = Fake('text')
    title = Fake('name')

    class Meta:
        model = Post
