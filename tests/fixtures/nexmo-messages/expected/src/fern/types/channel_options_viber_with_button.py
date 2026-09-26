

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .channel_options_viber_with_button_channel import ChannelOptionsViberWithButtonChannel
from .channel_options_viber_with_button_viber_service import ChannelOptionsViberWithButtonViberService
from .from_id import FromId
from .to_number import ToNumber


class ChannelOptionsViberWithButton(UniversalBaseModel):
    channel: typing.Optional[ChannelOptionsViberWithButtonChannel] = pydantic.Field(default=None)
    """
    The channel to send to. You must provide `viber_service` in this field
    """

    from_: typing_extensions.Annotated[
        typing.Optional[FromId], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    to: typing.Optional[ToNumber] = None
    viber_service: typing.Optional[ChannelOptionsViberWithButtonViberService] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
