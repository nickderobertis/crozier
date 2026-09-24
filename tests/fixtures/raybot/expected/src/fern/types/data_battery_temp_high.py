

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DataBatteryTempHigh(UniversalBaseModel):
    threshold: float = pydantic.Field()
    """
    The temperature threshold that triggered the alarm
    """

    temp: float = pydantic.Field()
    """
    The actual temperature that triggered the alarm
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
