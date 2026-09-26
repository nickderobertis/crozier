

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .from_id import FromId
from .inbound_messenger_message_common_channel import InboundMessengerMessageCommonChannel
from .message_uuid import MessageUuid
from .timestamp import Timestamp
from .to_id import ToId


class InboundMessengerMessageCommon(UniversalBaseModel):
    channel: InboundMessengerMessageCommonChannel = pydantic.Field()
    """
    The channel that the message came in on
    """

    from_: typing_extensions.Annotated[FromId, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    message_uuid: MessageUuid
    timestamp: Timestamp
    to: ToId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
