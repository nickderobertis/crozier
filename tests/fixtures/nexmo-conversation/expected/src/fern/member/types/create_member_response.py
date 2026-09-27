

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.channel import Channel
from ...types.href_member import HrefMember
from ...types.initiator import Initiator
from ...types.member_id import MemberId
from ...types.member_state import MemberState
from ...types.timestamp_res_member import TimestampResMember
from ...types.user_id import UserId


class CreateMemberResponse(UniversalBaseModel):
    channel: typing.Optional[Channel] = None
    href: typing.Optional[HrefMember] = None
    id: typing.Optional[MemberId] = None
    initiator: typing.Optional[Initiator] = None
    state: typing.Optional[MemberState] = None
    timestamp: typing.Optional[TimestampResMember] = None
    user_id: typing.Optional[UserId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
