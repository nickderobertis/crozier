

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .app import App
from .group_message_data_content import GroupMessageDataContent
from .group_message_data_settings import GroupMessageDataSettings
from .group_message_data_status import GroupMessageDataStatus
from .user import User


class GroupMessageData(UniversalBaseModel):
    app: typing.Optional[App] = None
    content: typing.Optional[GroupMessageDataContent] = None
    id: int
    message: typing.Optional["GroupMessage"] = None
    owner: typing.Optional[User] = None
    settings: typing.Optional[GroupMessageDataSettings] = None
    status: typing.Optional[GroupMessageDataStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .group import Group
from .group_message import GroupMessage

update_forward_refs(GroupMessageData, Group=Group, GroupMessage=GroupMessage)
