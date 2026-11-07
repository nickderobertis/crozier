

import typing

import pydantic
from ..category.types.category import Category
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pagination_metadata import PaginationMetadata


class PaginatedCategoryResponse(UniversalBaseModel):
    """
    Paginated list of categories
    """

    data: typing.Optional[typing.List[Category]] = None
    pagination: typing.Optional[PaginationMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
