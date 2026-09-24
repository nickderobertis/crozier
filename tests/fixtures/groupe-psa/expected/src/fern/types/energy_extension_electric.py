

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .energy_battery import EnergyBattery
from .energy_charging import EnergyCharging


class EnergyExtensionElectric(UniversalBaseModel):
    """
    Specific electric energy parameters.
    """

    battery: typing.Optional[EnergyBattery] = None
    charging: typing.Optional[EnergyCharging] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
