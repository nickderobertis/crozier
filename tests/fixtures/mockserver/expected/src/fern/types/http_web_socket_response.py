

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delay import Delay
from .http_web_socket_response_messages_item import HttpWebSocketResponseMessagesItem


class HttpWebSocketResponse(UniversalBaseModel):
    """
    WebSocket response to return
    """

    delay: typing.Optional[Delay] = None
    subprotocol: typing.Optional[str] = None
    messages: typing.Optional[typing.List[HttpWebSocketResponseMessagesItem]] = None
    close_connection: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="closeConnection"), pydantic.Field(alias="closeConnection")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
