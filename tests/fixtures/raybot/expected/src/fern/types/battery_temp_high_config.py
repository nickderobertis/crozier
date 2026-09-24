

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BatteryTempHighConfig(UniversalBaseModel):
    enable: bool = pydantic.Field()
    """
    Whether to enable battery temperature high monitoring
    """

    threshold: float = pydantic.Field()
    """
    The threshold temperature value for high battery temperature alert (°C)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
