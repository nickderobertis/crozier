

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .energy_battery_base import EnergyBatteryBase
from .energy_charging import EnergyCharging


class EnergyBaseExtensionElectric(UniversalBaseModel):
    """
    Specific electric energy parameters.
    """

    battery: typing.Optional[EnergyBatteryBase] = None
    charging: typing.Optional[EnergyCharging] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
