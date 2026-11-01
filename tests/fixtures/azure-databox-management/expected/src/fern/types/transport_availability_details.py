

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transport_availability_details_shipment_type import TransportAvailabilityDetailsShipmentType


class TransportAvailabilityDetails(UniversalBaseModel):
    """
    Transport options availability details for given region.
    """

    shipment_type: typing_extensions.Annotated[
        typing.Optional[TransportAvailabilityDetailsShipmentType],
        FieldMetadata(alias="shipmentType"),
        pydantic.Field(alias="shipmentType", description="Transport Shipment Type supported for given region."),
    ] = None
    """
    Transport Shipment Type supported for given region.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
