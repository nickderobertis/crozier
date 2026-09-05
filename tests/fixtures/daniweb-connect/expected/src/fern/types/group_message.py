

from __future__ import annotations

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .group_message_last_seen import GroupMessageLastSeen
from .group_message_moderated import GroupMessageModerated
from .group_message_text import GroupMessageText
from .user import User


class GroupMessage(UniversalBaseModel):
    author: typing.Optional[User] = None
    group: typing.Optional["Group"] = None
    id: int
    last_seen: typing.Optional[GroupMessageLastSeen] = None
    moderated: typing.Optional[GroupMessageModerated] = None
    text: typing.Optional[GroupMessageText] = None
    timestamp: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group import Group

update_forward_refs(GroupMessage, Group=Group)
