

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .endpoint_post_groups_id_schedules_data_item_navigation import EndpointPostGroupsIdSchedulesDataItemNavigation


class EndpointPostGroupsIdSchedulesDataItem(UniversalBaseModel):
    author_count: typing.Optional[int] = None
    date: typing.Optional[dt.date] = None
    first_message: typing.Optional["GroupMessage"] = None
    group_count: typing.Optional[int] = None
    group_id: typing.Optional[int] = None
    last_message: typing.Optional["GroupMessage"] = None
    message_count: typing.Optional[int] = None
    my_message_count: typing.Optional[int] = None
    navigation: typing.Optional[EndpointPostGroupsIdSchedulesDataItemNavigation] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group import Group
from .group_message import GroupMessage

update_forward_refs(EndpointPostGroupsIdSchedulesDataItem, Group=Group, GroupMessage=GroupMessage)
