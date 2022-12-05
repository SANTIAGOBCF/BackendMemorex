from faketory.factory import Faketory
from faketory.gens import Fake, FaketoryGen

from politician.models import Politician
from user.tests.factories import FactoryUser


class FactoryPolitician(Faketory):
    approver = FaketoryGen(
        FactoryUser,
        _resolver="save",
    )
    creator = FaketoryGen(
        FactoryUser,
        _resolver="save",
    )
    description = Fake('text')
    name = Fake('name')
    organization = Fake('name')
    profile_image = Fake('image_url')
    reference = Fake('image_url')

    class Meta:
        model = Politician
