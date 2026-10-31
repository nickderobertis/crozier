

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transport_availability_details import TransportAvailabilityDetails


class TransportAvailabilityResponse(UniversalBaseModel):
    """
    Transport options available for given sku in a region.
    """

    transport_availability_details: typing_extensions.Annotated[
        typing.Optional[typing.List[TransportAvailabilityDetails]],
        FieldMetadata(alias="transportAvailabilityDetails"),
        pydantic.Field(
            alias="transportAvailabilityDetails", description="List of transport availability details for given region"
        ),
    ] = None
    """
    List of transport availability details for given region
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
