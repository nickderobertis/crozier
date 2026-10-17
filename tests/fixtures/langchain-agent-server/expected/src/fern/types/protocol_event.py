

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .protocol_event_params import ProtocolEventParams
from .protocol_event_type import ProtocolEventType


class ProtocolEvent(UniversalBaseModel):
    """
    A server → client event. Sent as JSON over WebSocket, or as the `data:` field of an SSE frame (with `event:` set to `method` and `id:` set to `seq`).
    """

    type: ProtocolEventType
    event_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique ID for reconnection (mirrored to SSE `id:`).
    """

    seq: typing.Optional[int] = pydantic.Field(default=None)
    """
    Monotonic per-session sequence number for ordering and replay.
    """

    method: str = pydantic.Field()
    """
    Channel method name (e.g. `messages`, `tools`, `lifecycle`, `custom:my_channel`).
    """

    params: ProtocolEventParams

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
