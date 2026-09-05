

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_get_groups_id_memberships_data_item_privileges import EndpointGetGroupsIdMembershipsDataItemPrivileges
from .user import User


class EndpointGetGroupsIdMembershipsDataItem(UniversalBaseModel):
    group: typing.Optional["Group"] = None
    member: typing.Optional[User] = None
    privileges: typing.Optional[EndpointGetGroupsIdMembershipsDataItemPrivileges] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group import Group
from .group_message import GroupMessage

update_forward_refs(EndpointGetGroupsIdMembershipsDataItem, Group=Group, GroupMessage=GroupMessage)
