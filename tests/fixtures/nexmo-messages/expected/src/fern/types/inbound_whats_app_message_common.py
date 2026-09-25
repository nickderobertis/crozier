

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .context import Context
from .from_number import FromNumber
from .inbound_whats_app_message_common_channel import InboundWhatsAppMessageCommonChannel
from .message_uuid import MessageUuid
from .profile import Profile
from .timestamp import Timestamp
from .to_number import ToNumber


class InboundWhatsAppMessageCommon(UniversalBaseModel):
    channel: InboundWhatsAppMessageCommonChannel = pydantic.Field()
    """
    The channel that the message came in on
    """

    context: typing.Optional[Context] = None
    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    message_uuid: MessageUuid
    profile: typing.Optional[Profile] = None
    provider_message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A message from the channel provider, which may contain a description, error codes or other information
    """

    timestamp: Timestamp
    to: ToNumber

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
