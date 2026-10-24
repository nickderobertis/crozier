

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paginated_routes_response_object import PaginatedRoutesResponseObject
from .pagination_info import PaginationInfo
from .route import Route


class PaginatedRoutesResponse(UniversalBaseModel):
    object: PaginatedRoutesResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[Route] = pydantic.Field()
    """
    Array of routes
    """

    pagination: PaginationInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
