

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_options_messenger_channel import ChannelOptionsMessengerChannel
from .channel_options_messenger_messenger import ChannelOptionsMessengerMessenger
from .from_id import FromId
from .to_id import ToId


class ChannelOptionsMessenger(UniversalBaseModel):
    channel: typing.Optional[ChannelOptionsMessengerChannel] = pydantic.Field(default=None)
    """
    The channel to send to. You must provide `messenger` in this field
    """

    from_: typing_extensions.Annotated[
        typing.Optional[FromId], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    messenger: typing.Optional[ChannelOptionsMessengerMessenger] = None
    to: typing.Optional[ToId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
