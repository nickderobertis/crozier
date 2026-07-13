

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .groups_v2group_v2 import GroupsV2GroupV2


class GroupsV2GroupMembershipBase(UniversalBaseModel):
    group: typing.Optional[GroupsV2GroupV2] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
