

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .energy_extension_electric import EnergyExtensionElectric
from .energy_extension_fuel import EnergyExtensionFuel


class EnergyExtension(UniversalBaseModel):
    fuel: typing.Optional[EnergyExtensionFuel] = pydantic.Field(default=None)
    """
    Specific fuel energy properties.
    """

    electric: typing.Optional[EnergyExtensionElectric] = pydantic.Field(default=None)
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
