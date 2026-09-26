

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .from_number import FromNumber
from .inbound_viber_message_common_channel import InboundViberMessageCommonChannel
from .inbound_viber_message_common_context import InboundViberMessageCommonContext
from .message_uuid import MessageUuid
from .timestamp import Timestamp
from .to_id import ToId


class InboundViberMessageCommon(UniversalBaseModel):
    channel: InboundViberMessageCommonChannel = pydantic.Field()
    """
    The channel that the message came in on
    """

    context: typing.Optional[InboundViberMessageCommonContext] = pydantic.Field(default=None)
    """
    Object containing contextual details for the inbound message when it is a response to another message.
    """

    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
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
