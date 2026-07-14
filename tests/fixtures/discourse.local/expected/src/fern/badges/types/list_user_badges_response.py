

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .list_user_badges_response_badge_types_item import ListUserBadgesResponseBadgeTypesItem
from .list_user_badges_response_badges_item import ListUserBadgesResponseBadgesItem
from .list_user_badges_response_granted_bies_item import ListUserBadgesResponseGrantedBiesItem
from .list_user_badges_response_user_badges_item import ListUserBadgesResponseUserBadgesItem


class ListUserBadgesResponse(UniversalBaseModel):
    badge_types: typing.Optional[typing.List[ListUserBadgesResponseBadgeTypesItem]] = None
    badges: typing.Optional[typing.List[ListUserBadgesResponseBadgesItem]] = None
    granted_bies: typing.Optional[typing.List[ListUserBadgesResponseGrantedBiesItem]] = None
    user_badges: typing.List[ListUserBadgesResponseUserBadgesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
