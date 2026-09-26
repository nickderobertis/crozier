

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BasicKinetic(UniversalBaseModel):
    """
    Everything related to the movement of the vehicle. Speed, acceleration..
    """

    acceleration: typing.Optional[float] = pydantic.Field(default=None)
    """
    Vehicle acceleration (expressed in m/s²)
    """

    speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    Vehicle speed (expressed in km/h)
    """

    moving: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
