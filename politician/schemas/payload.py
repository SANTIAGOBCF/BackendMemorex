from typing import Optional

from ninja import Schema


class PayloadPatchPolitician(Schema):
    description: Optional[str]
    name: Optional[str]
    organization: Optional[str]
    profile_image: Optional[str]
    reference: Optional[str]


class PayloadPostAddPolitician(Schema):
    description: str
    name: str
    organization: str
    profile_image: str
    reference: str
