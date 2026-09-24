

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .onboard_capabilities import OnboardCapabilities
from .vehicle_branding import VehicleBranding
from .vehicle_pictures import VehiclePictures


class VehicleExtension(UniversalBaseModel):
    """
    Additional vehicle  information.
    """

    onboard_capabilities: typing_extensions.Annotated[
        typing.Optional[OnboardCapabilities],
        FieldMetadata(alias="onboardCapabilities"),
        pydantic.Field(alias="onboardCapabilities"),
    ] = None
    branding: typing.Optional[VehicleBranding] = None
    pictures: typing.Optional[VehiclePictures] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
