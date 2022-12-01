from ninja import Router

from .constants import Endpoints

router = Router()


@router.get(
    Endpoints.GET_POLITICIAN,
    response=str,
)
def get_politician(request):
    return 'politician'
