

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompositFuelEnergyConsumption(UniversalBaseModel):
    """
    Fuel consumption.
    """

    total: typing.Optional[float] = pydantic.Field(default=None)
    """
    Total Fuel consumption expressed in cL.
    """

    instant: typing.Optional[float] = pydantic.Field(default=None)
    """
    Instant Fuel consumption.
    * If subType equal to FossilEnergy than it will be expressed in L/100Km.
    * If subType equal to Hydrogen than it will be expressed in Kg/100Km.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
