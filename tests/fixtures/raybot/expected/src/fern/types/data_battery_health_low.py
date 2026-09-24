

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DataBatteryHealthLow(UniversalBaseModel):
    threshold: float = pydantic.Field()
    """
    The battery health threshold that triggered the alarm
    """

    health: float = pydantic.Field()
    """
    The actual battery health that triggered the alarm
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
