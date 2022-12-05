from typing import List

from ninja import Schema

from .common import SchemaPolitician


class ResponseGetPolitician(SchemaPolitician):
    pass


class ResponsePatchPolitician(SchemaPolitician):
    pass


class ResponseGetPoliticianList(Schema):
    politician_list: List[ResponseGetPolitician]
    count: int


class ResponsePostAddPolitician(SchemaPolitician):
    pass
