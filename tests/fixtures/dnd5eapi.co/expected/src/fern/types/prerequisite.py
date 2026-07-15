

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .api_reference import ApiReference


class Prerequisite(UniversalBaseModel):
    """
    `Prerequisite`
    """

    ability_score: typing.Optional[ApiReference] = None
    minimum_score: typing.Optional[float] = pydantic.Field(default=None)
    """
    Minimum score to meet the prerequisite.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
