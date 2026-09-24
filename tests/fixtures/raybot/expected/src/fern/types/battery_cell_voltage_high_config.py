

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BatteryCellVoltageHighConfig(UniversalBaseModel):
    enable: bool = pydantic.Field()
    """
    Whether to enable battery cell voltage high monitoring
    """

    threshold: float = pydantic.Field()
    """
    The threshold voltage value for high battery cell voltage alert (V)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
