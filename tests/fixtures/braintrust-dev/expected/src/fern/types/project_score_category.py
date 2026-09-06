

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProjectScoreCategory(UniversalBaseModel):
    """
    For categorical-type project scores, defines a single category
    """

    name: str = pydantic.Field()
    """
    Name of the category
    """

    value: float = pydantic.Field()
    """
    Numerical value of the category. Must be between 0 and 1, inclusive
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
