

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .paginated_suppressions_response_object import PaginatedSuppressionsResponseObject
from .pagination_info import PaginationInfo
from .suppression import Suppression


class PaginatedSuppressionsResponse(UniversalBaseModel):
    object: PaginatedSuppressionsResponseObject = pydantic.Field()
    """
    Object type identifier
    """

    data: typing.List[Suppression] = pydantic.Field()
    """
    Array of suppressions
    """

    pagination: PaginationInfo

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
