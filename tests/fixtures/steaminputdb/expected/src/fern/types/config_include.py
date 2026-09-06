

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConfigInclude(UniversalBaseModel):
    tags: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include tags
    """

    votes: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include vote data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
