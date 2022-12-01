import uuid

from django.db import models

from core.models import TimeStampedModel
from user.models import User


class Politician(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # ForeignKeys
    approver = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='approver'
    )
    creator = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name='creator'
    )

    description = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    profile_image = models.CharField(max_length=100)
    reference = models.CharField(max_length=100)
