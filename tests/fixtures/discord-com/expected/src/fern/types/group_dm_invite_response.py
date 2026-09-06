

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .invite_channel_response import InviteChannelResponse
from .user_response import UserResponse


class GroupDmInviteResponse(UniversalBaseModel):
    type: typing.Optional[int] = None
    code: str
    inviter: typing.Optional[UserResponse] = None
    max_age: typing.Optional[int] = None
    created_at: typing.Optional[dt.datetime] = None
    expires_at: typing.Optional[dt.datetime] = None
    channel: typing.Optional[InviteChannelResponse] = None
    approximate_member_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
