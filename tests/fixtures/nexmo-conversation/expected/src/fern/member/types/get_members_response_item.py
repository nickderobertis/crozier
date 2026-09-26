

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.member_state import MemberState
from ...types.name_user import NameUser
from ...types.user_id import UserId


class GetMembersResponseItem(UniversalBaseModel):
    name: NameUser
    state: MemberState
    user_id: UserId
    user_name: NameUser

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
