

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .composit_fuel_energy_consumption import CompositFuelEnergyConsumption


class EnergyExtensionFuel(UniversalBaseModel):
    """
    Specific fuel energy properties.
    """

    consumptions: typing.Optional[CompositFuelEnergyConsumption] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
