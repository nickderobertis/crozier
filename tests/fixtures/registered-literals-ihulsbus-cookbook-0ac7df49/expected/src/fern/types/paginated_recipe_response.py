

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..recipe.types.recipe import Recipe
from .pagination_metadata import PaginationMetadata


class PaginatedRecipeResponse(UniversalBaseModel):
    """
    Paginated list of recipes
    """

    data: typing.Optional[typing.List[Recipe]] = None
    pagination: typing.Optional[PaginationMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
