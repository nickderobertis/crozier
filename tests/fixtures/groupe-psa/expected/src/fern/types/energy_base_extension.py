

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .energy_base_extension_electric import EnergyBaseExtensionElectric
from .energy_base_extension_fuel import EnergyBaseExtensionFuel


class EnergyBaseExtension(UniversalBaseModel):
    fuel: typing.Optional[EnergyBaseExtensionFuel] = pydantic.Field(default=None)
    """
    Specific fuel energy properties.
    """

    electric: typing.Optional[EnergyBaseExtensionElectric] = pydantic.Field(default=None)
    """
    Specific electric energy parameters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
