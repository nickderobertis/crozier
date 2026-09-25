

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BatteryBase(UniversalBaseModel):
    """
    Describe the car (with combustion engine)  battery status.
    """

    voltage: typing.Optional[float] = pydantic.Field(default=None)
    """
    Auxiliary battery (12V) state of health in %
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
