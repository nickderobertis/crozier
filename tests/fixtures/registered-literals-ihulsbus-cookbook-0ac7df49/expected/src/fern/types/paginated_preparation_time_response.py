

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..preparationtime.types.preparation_time import PreparationTime
from .pagination_metadata import PaginationMetadata


class PaginatedPreparationTimeResponse(UniversalBaseModel):
    """
    Paginated list of preparation times
    """

    data: typing.Optional[typing.List[PreparationTime]] = None
    pagination: typing.Optional[PaginationMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
