

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .member import Member
from .user_business_card import UserBusinessCard
from .user_profile import UserProfile
from .user_usage import UserUsage


class User(UniversalBaseModel):
    business_card: typing.Optional[UserBusinessCard] = None
    community_persona: typing.Optional[Member] = None
    id: int
    profile: typing.Optional[UserProfile] = None
    usage: typing.Optional[UserUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
