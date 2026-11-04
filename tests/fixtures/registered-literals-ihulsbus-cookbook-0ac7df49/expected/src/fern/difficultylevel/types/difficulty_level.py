

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DifficultyLevel(UniversalBaseModel):
    """
    Information about a Dificulty Level
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of a Dificulty Level
    """

    level: typing.Optional[int] = pydantic.Field(default=None)
    """
    name of a Dificulty Level
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
