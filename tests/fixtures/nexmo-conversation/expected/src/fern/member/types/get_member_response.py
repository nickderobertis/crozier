

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.href_member import HrefMember
from ...types.member_id import MemberId


class GetMemberResponse(UniversalBaseModel):
    href: typing.Optional[HrefMember] = None
    id: typing.Optional[MemberId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
