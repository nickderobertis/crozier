

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class StreamServicesCapabilityResponseStreamServicesItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Streaming service identifier
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version of the streaming service integration
    """

    quality: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of supported audio quality levels for this service
    """

    replay_gain: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="replayGain"),
        pydantic.Field(
            alias="replayGain", description="Indicates if replay gain is supported for this service (optional)"
        ),
    ] = None
    """
    Indicates if replay gain is supported for this service (optional)
    """

    configurable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the service is configurable (optional)
    """

    active: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates if the service is currently active (optional)
    """

    brand: typing.Optional[str] = pydantic.Field(default=None)
    """
    Brand associated with the service (optional)
    """

    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model associated with the service (optional)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
