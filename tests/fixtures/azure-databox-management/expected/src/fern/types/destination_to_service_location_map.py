

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinationToServiceLocationMap(UniversalBaseModel):
    """
    Map of destination location to service location.
    """

    destination_location: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="destinationLocation"),
        pydantic.Field(alias="destinationLocation", description="Location of the destination."),
    ] = None
    """
    Location of the destination.
    """

    service_location: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serviceLocation"),
        pydantic.Field(alias="serviceLocation", description="Location of the service."),
    ] = None
    """
    Location of the service.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
