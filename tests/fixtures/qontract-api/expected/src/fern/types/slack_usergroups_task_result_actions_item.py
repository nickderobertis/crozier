

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .slack_usergroup_action_update_users_notifications_item import SlackUsergroupActionUpdateUsersNotificationsItem


class SlackUsergroupsTaskResultActionsItem_Create(UniversalBaseModel):
    action_type: typing.Literal["create"] = "create"
    description: str
    usergroup: str
    users: typing.List[str]
    workspace: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SlackUsergroupsTaskResultActionsItem_UpdateUsers(UniversalBaseModel):
    action_type: typing.Literal["update_users"] = "update_users"
    notifications: typing.Optional[typing.List[SlackUsergroupActionUpdateUsersNotificationsItem]] = None
    usergroup: str
    users: typing.List[str]
    users_to_add: typing.List[str]
    users_to_remove: typing.List[str]
    workspace: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class SlackUsergroupsTaskResultActionsItem_UpdateMetadata(UniversalBaseModel):
    action_type: typing.Literal["update_metadata"] = "update_metadata"
    channels: typing.List[str]
    description: str
    usergroup: str
    workspace: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


SlackUsergroupsTaskResultActionsItem = typing_extensions.Annotated[
    typing.Union[
        SlackUsergroupsTaskResultActionsItem_Create,
        SlackUsergroupsTaskResultActionsItem_UpdateUsers,
        SlackUsergroupsTaskResultActionsItem_UpdateMetadata,
    ],
    pydantic.Field(discriminator="action_type"),
]
