

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .stream_services_capability_response_stream_services_item import StreamServicesCapabilityResponseStreamServicesItem


class StreamServicesCapabilityResponse(UniversalBaseModel):
    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    API version
    """

    encrypt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Encryption version
    """

    stream_services: typing_extensions.Annotated[
        typing.Optional[typing.List[StreamServicesCapabilityResponseStreamServicesItem]],
        FieldMetadata(alias="streamServices"),
        pydantic.Field(
            alias="streamServices", description="List of supported streaming services and their capabilities"
        ),
    ] = None
    """
    List of supported streaming services and their capabilities
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
