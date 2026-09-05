

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_patch_groups_id_memberships_data_item_privileges import (
    EndpointPatchGroupsIdMembershipsDataItemPrivileges,
)
from .user import User


class EndpointPatchGroupsIdMembershipsDataItem(UniversalBaseModel):
    group: typing.Optional["Group"] = None
    member: typing.Optional[User] = None
    privileges: typing.Optional[EndpointPatchGroupsIdMembershipsDataItemPrivileges] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group import Group
from .group_message import GroupMessage

update_forward_refs(EndpointPatchGroupsIdMembershipsDataItem, Group=Group, GroupMessage=GroupMessage)
