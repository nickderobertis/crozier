

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .slack_usergroup_action_update_users_notifications_item import SlackUsergroupActionUpdateUsersNotificationsItem


class SlackUsergroupActionUpdateUsers(UniversalBaseModel):
    """
    Action: Update usergroup users.
    """

    notifications: typing.Optional[typing.List[SlackUsergroupActionUpdateUsersNotificationsItem]] = pydantic.Field(
        default=None
    )
    """
    Notification actions triggered on membership changes
    """

    usergroup: str = pydantic.Field()
    """
    Usergroup handle/name
    """

    users: typing.List[str] = pydantic.Field()
    """
    List of users after update
    """

    users_to_add: typing.List[str] = pydantic.Field()
    """
    List of users to add
    """

    users_to_remove: typing.List[str] = pydantic.Field()
    """
    List of users to remove
    """

    workspace: str = pydantic.Field()
    """
    Workspace name
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
