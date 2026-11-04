

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PreparationTime(UniversalBaseModel):
    """
    Information about a Peparation Time
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of a Peparation Time
    """

    duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    name of a Peparation Time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
