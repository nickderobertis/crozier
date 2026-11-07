

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..difficultylevel.types.difficulty_level import DifficultyLevel
from .pagination_metadata import PaginationMetadata


class PaginatedDifficultyLevelResponse(UniversalBaseModel):
    """
    Paginated list of difficulty levels
    """

    data: typing.Optional[typing.List[DifficultyLevel]] = None
    pagination: typing.Optional[PaginationMetadata] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
