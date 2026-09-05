

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .member_identity import MemberIdentity
from .member_location import MemberLocation
from .member_personal import MemberPersonal
from .member_signature import MemberSignature
from .member_stats import MemberStats


class Member(UniversalBaseModel):
    id: int
    identity: typing.Optional[MemberIdentity] = None
    location: typing.Optional[MemberLocation] = None
    personal: typing.Optional[MemberPersonal] = None
    signature: typing.Optional[MemberSignature] = None
    stats: typing.Optional[MemberStats] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
