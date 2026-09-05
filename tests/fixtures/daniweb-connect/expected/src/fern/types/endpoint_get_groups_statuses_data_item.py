

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class EndpointGetGroupsStatusesDataItem(UniversalBaseModel):
    earliest_unseen_message: typing.Optional["GroupMessage"] = None
    group: typing.Optional["Group"] = None
    new_message_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group import Group
from .group_message import GroupMessage

update_forward_refs(EndpointGetGroupsStatusesDataItem, Group=Group, GroupMessage=GroupMessage)
