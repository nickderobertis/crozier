

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .vehicle_branding_single import VehicleBrandingSingle
from .vehicle_pictures import VehiclePictures


class VehicleExtensions(UniversalBaseModel):
    """
    Additional vehicle  information.
    """

    branding: typing.Optional[VehicleBrandingSingle] = None
    pictures: typing.Optional[VehiclePictures] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
