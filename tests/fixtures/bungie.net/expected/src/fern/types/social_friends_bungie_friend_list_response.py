

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .social_friends_bungie_friend import SocialFriendsBungieFriend


class SocialFriendsBungieFriendListResponse(UniversalBaseModel):
    friends: typing.Optional[typing.List[SocialFriendsBungieFriend]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
