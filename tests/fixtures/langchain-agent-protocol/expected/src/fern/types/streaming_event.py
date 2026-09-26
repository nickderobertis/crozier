

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .streaming_event_type import StreamingEventType


class StreamingEvent(UniversalBaseModel):
    """
    Server-to-client event in the streaming protocol.
    """

    type: StreamingEventType
    event_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="eventId"),
        pydantic.Field(
            alias="eventId", description="Unique event ID used for reconnection. Maps to the SSE `id:` field."
        ),
    ] = None
    """
    Unique event ID used for reconnection. Maps to the SSE `id:` field.
    """

    seq: typing.Optional[int] = pydantic.Field(default=None)
    """
    Monotonic sequence number for ordering and replay.
    """

    method: str = pydantic.Field()
    """
    Event method. Most events use the channel name, while some event families use a more specific method such as `input.requested`.
    """

    params: typing.Dict[str, typing.Any] = pydantic.Field()
    """
    Event parameters, including namespace, timestamp, and channel-specific data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
