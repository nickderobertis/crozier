

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_electric_energy import HealthElectricEnergy
from .load_electric_energy import LoadElectricEnergy


class EnergyBatteryBase(UniversalBaseModel):
    """
    Electric battery capacity and heath
    """

    load: typing.Optional[LoadElectricEnergy] = None
    health: typing.Optional[HealthElectricEnergy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
