

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .schedule_availability_response import ScheduleAvailabilityResponse
from .transport_availability_response import TransportAvailabilityResponse


class RegionConfigurationResponse(UniversalBaseModel):
    """
    Configuration response specific to a region.
    """

    schedule_availability_response: typing_extensions.Annotated[
        typing.Optional[ScheduleAvailabilityResponse],
        FieldMetadata(alias="scheduleAvailabilityResponse"),
        pydantic.Field(
            alias="scheduleAvailabilityResponse", description="Schedule availability for given sku in a region."
        ),
    ] = None
    """
    Schedule availability for given sku in a region.
    """

    transport_availability_response: typing_extensions.Annotated[
        typing.Optional[TransportAvailabilityResponse],
        FieldMetadata(alias="transportAvailabilityResponse"),
        pydantic.Field(
            alias="transportAvailabilityResponse", description="Transport options available for given sku in a region."
        ),
    ] = None
    """
    Transport options available for given sku in a region.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
