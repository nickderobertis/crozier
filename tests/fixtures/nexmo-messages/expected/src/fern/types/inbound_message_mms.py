

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .from_number import FromNumber
from .inbound_message_mms_channel import InboundMessageMmsChannel
from .message_uuid import MessageUuid
from .timestamp import Timestamp
from .to_number import ToNumber


class InboundMessageMms(UniversalBaseModel):
    channel: InboundMessageMmsChannel = pydantic.Field()
    """
    The channel the message came in on
    """

    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    message_uuid: MessageUuid
    timestamp: Timestamp
    to: ToNumber

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
