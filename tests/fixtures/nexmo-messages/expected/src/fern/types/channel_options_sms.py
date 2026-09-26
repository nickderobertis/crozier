

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_options_sms_channel import ChannelOptionsSmsChannel
from .from_number import FromNumber
from .to_number import ToNumber


class ChannelOptionsSms(UniversalBaseModel):
    channel: typing.Optional[ChannelOptionsSmsChannel] = pydantic.Field(default=None)
    """
    The channel to send to. You must provide `sms` in this field
    """

    from_: typing_extensions.Annotated[
        typing.Optional[FromNumber], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    to: typing.Optional[ToNumber] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
