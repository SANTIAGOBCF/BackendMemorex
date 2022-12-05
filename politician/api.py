from django.shortcuts import get_object_or_404
from ninja import Query, Router

from core.filters import FilterPagination
from core.utils import get_paginated_queryset
from politician.models import Politician
from user.bearers import AuthBearer

from .constants import Endpoints
from .schemas.payload import PayloadPatchPolitician, PayloadPostAddPolitician
from .schemas.response import (ResponseGetPolitician,
                               ResponseGetPoliticianList,
                               ResponsePostAddPolitician)

router = Router()


@router.get(
    Endpoints.GET_POLITICIAN,
    response=ResponseGetPolitician,
)
def get_politician(request, id):
    return get_object_or_404(Politician, id=id)


@router.patch(
    Endpoints.PATCH_POLITICIAN,
    auth=AuthBearer(),
    response=ResponseGetPolitician,
)
def patch_politician(request, data: PayloadPatchPolitician, id):
    """
    Edit politician by id.
    """
    politician = get_object_or_404(Politician, id=id)
    patch_data = data.dict(exclude_unset=True)
    for key, value in patch_data.items():
        setattr(politician, key, value)
    return politician


@router.get(
    Endpoints.GET_POLITICIAN_LIST,
    response=ResponseGetPoliticianList,
)
def get_politician_list(request, data: FilterPagination = Query(...)):
    queryset = Politician.objects.all()
    count = queryset.count()
    queryset = get_paginated_queryset(queryset, data.limit, data.offset)
    return {'politician_list': list(queryset), 'count': count}


@router.post(
    Endpoints.POST_ADD_POLICIAN,
    auth=AuthBearer(),
    response={201: ResponsePostAddPolitician},
)
def add_politician(request, data: PayloadPostAddPolitician):
    """
    Create a new politician.
    """
    politician_data = data.dict()
    politician_data['creator_id'] = request.user.id

    return Politician.objects.create(**politician_data)
