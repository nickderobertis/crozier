

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..cuisinetype.types.cuisine_type import CuisineType
from .pagination_metadata import PaginationMetadata


class PaginatedCuisineTypeResponse(UniversalBaseModel):
    """
    Paginated list of cuisine types
    """

    data: typing.Optional[typing.List[CuisineType]] = None
    pagination: typing.Optional[PaginationMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
