

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_from_websocket_content_type import ChannelFromWebsocketContentType
from .channel_from_websocket_headers import ChannelFromWebsocketHeaders


class ChannelFromWebsocket(UniversalBaseModel):
    """
    Connect to a Websocket
    """

    content_type: typing_extensions.Annotated[
        ChannelFromWebsocketContentType, FieldMetadata(alias="content-type"), pydantic.Field(alias="content-type")
    ]
    headers: typing.Optional[ChannelFromWebsocketHeaders] = pydantic.Field(default=None)
    """
    Details of the Websocket you want to connect to
    """

    uri: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
