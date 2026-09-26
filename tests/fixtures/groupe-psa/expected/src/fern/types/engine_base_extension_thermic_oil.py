

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EngineBaseExtensionThermicOil(UniversalBaseModel):
    """
    Engine oil properties.
    """

    level: typing.Optional[int] = pydantic.Field(default=None)
    """
    Engine liquid level expressed in persent.
    """

    temp: typing.Optional[float] = pydantic.Field(default=None)
    """
    Engine liquid temperature expressed in Celsius degrees.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
