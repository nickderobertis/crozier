

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .kinetic import Kinetic
from .vehicle_odometer import VehicleOdometer


class Extension(UniversalBaseModel):
    """
    Additional data set.
    """

    odometer: typing.Optional[VehicleOdometer] = None
    kinetic: typing.Optional[Kinetic] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
