

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .energy_battery_health import EnergyBatteryHealth
from .energy_battery_load import EnergyBatteryLoad


class EnergyBattery(UniversalBaseModel):
    """
    Electric charging state.
    """

    load: typing.Optional[EnergyBatteryLoad] = None
    health: typing.Optional[EnergyBatteryHealth] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
