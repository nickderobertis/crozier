

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .channel_options_mms_channel import ChannelOptionsMmsChannel
from .from_number import FromNumber
from .to_number import ToNumber
from .v_card import VCard


class SendMessageRequestOneOne(VCard):
    to: ToNumber
    from_: typing_extensions.Annotated[FromNumber, FieldMetadata(alias="from"), pydantic.Field(alias="from")]
    channel: ChannelOptionsMmsChannel = pydantic.Field()
    """
    The channel to send to. You must provide `mms` in this field
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
