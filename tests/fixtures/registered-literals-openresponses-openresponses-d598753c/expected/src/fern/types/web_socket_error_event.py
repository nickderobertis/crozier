

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .web_socket_error_event_error import WebSocketErrorEventError
from .web_socket_error_event_type import WebSocketErrorEventType


class WebSocketErrorEvent(UniversalBaseModel):
    """
    A WebSocket error envelope returned for Responses WebSocket mode failures.
    """

    type: WebSocketErrorEventType = pydantic.Field()
    """
    The event type. Always `error`.
    """

    status: int = pydantic.Field()
    """
    The HTTP-style status code for the WebSocket error.
    """

    error: WebSocketErrorEventError = pydantic.Field()
    """
    The WebSocket error payload.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
