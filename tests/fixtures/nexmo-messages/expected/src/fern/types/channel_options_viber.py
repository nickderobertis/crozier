

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_options_viber_channel import ChannelOptionsViberChannel
from .channel_options_viber_viber_service import ChannelOptionsViberViberService
from .from_id import FromId
from .to_number import ToNumber


class ChannelOptionsViber(UniversalBaseModel):
    channel: typing.Optional[ChannelOptionsViberChannel] = pydantic.Field(default=None)
    """
    The channel to send to. You must provide `viber_service` in this field
    """

    from_: typing_extensions.Annotated[
        typing.Optional[FromId], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    to: typing.Optional[ToNumber] = None
    viber_service: typing.Optional[ChannelOptionsViberViberService] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
