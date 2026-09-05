

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .channel_types import ChannelTypes
from .invite_channel_recipient_response import InviteChannelRecipientResponse
from .snowflake_type import SnowflakeType


class InviteChannelResponse(UniversalBaseModel):
    id: SnowflakeType
    type: ChannelTypes
    name: typing.Optional[str] = None
    icon: typing.Optional[str] = None
    recipients: typing.Optional[typing.List[InviteChannelRecipientResponse]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
