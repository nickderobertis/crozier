

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .vehicle_capabilities_embedded import VehicleCapabilitiesEmbedded
from .vehicle_capabilities_motorization import VehicleCapabilitiesMotorization


class VehicleCapabilities(UniversalBaseModel):
    vin: str = pydantic.Field()
    """
    Serial number of a vehicle
    """

    motorization: typing.Optional[VehicleCapabilitiesMotorization] = pydantic.Field(default=None)
    """
    Motorization of the vehicle.
    """

    embedded: typing_extensions.Annotated[
        typing.Optional[VehicleCapabilitiesEmbedded],
        FieldMetadata(alias="_embedded"),
        pydantic.Field(alias="_embedded"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
