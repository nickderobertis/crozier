

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_list_badges_response_admin_badges import AdminListBadgesResponseAdminBadges
from .admin_list_badges_response_badge_groupings_item import AdminListBadgesResponseBadgeGroupingsItem
from .admin_list_badges_response_badge_types_item import AdminListBadgesResponseBadgeTypesItem
from .admin_list_badges_response_badges_item import AdminListBadgesResponseBadgesItem


class AdminListBadgesResponse(UniversalBaseModel):
    admin_badges: AdminListBadgesResponseAdminBadges
    badge_groupings: typing.List[AdminListBadgesResponseBadgeGroupingsItem]
    badge_types: typing.List[AdminListBadgesResponseBadgeTypesItem]
    badges: typing.List[AdminListBadgesResponseBadgesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
