

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..ingredient.types.ingredient import Ingredient
from .pagination_metadata import PaginationMetadata


class PaginatedIngredientResponse(UniversalBaseModel):
    """
    Paginated list of ingredients
    """

    data: typing.Optional[typing.List[Ingredient]] = None
    pagination: typing.Optional[PaginationMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
