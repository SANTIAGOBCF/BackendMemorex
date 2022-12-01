import uuid

from django.db import models

from core.models import TimeStampedModel
from politician.models import Politician
from user.models import User


class Post(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    politician = models.ForeignKey(Politician, on_delete=models.CASCADE)

    date = models.DateField()
    image = models.CharField(max_length=100)
    source = models.CharField(max_length=200)
    text = models.CharField(max_length=450)
    title = models.CharField(max_length=50)
