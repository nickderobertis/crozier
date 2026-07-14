

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .admin_list_badges_response_admin_badges_triggers import AdminListBadgesResponseAdminBadgesTriggers


class AdminListBadgesResponseAdminBadges(UniversalBaseModel):
    badge_grouping_ids: typing.List[typing.Optional[typing.Any]]
    badge_ids: typing.List[typing.Optional[typing.Any]]
    badge_type_ids: typing.List[typing.Optional[typing.Any]]
    protected_system_fields: typing.List[typing.Optional[typing.Any]]
    triggers: AdminListBadgesResponseAdminBadgesTriggers

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
