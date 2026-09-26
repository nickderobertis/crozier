

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .member_role import MemberRole
from .member_user import MemberUser


class Member(UniversalBaseModel):
    user: MemberUser
    role: MemberRole
    status: str
    joined_at: dt.datetime
    invited_by: typing.Optional[str] = None
    invited_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
