

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HealthElectricEnergy(UniversalBaseModel):
    capacity: typing.Optional[int] = pydantic.Field(default=None)
    """
    Health related to battery capacity (expressed in percentage).
    """

    resistance: typing.Optional[int] = pydantic.Field(default=None)
    """
    Health related to battery resistance (expressed in percentage).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
