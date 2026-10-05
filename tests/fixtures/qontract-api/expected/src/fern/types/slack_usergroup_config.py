

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .slack_usergroup_config_notifications_item import SlackUsergroupConfigNotificationsItem


class SlackUsergroupConfig(UniversalBaseModel):
    """
    Desired state configuration for a single Slack usergroup.
    """

    channels: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of channel names (e.g., #general, team-channel)
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Usergroup description
    """

    notifications: typing.Optional[typing.List[SlackUsergroupConfigNotificationsItem]] = pydantic.Field(default=None)
    """
    Notification actions triggered on membership changes
    """

    users: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of user emails (e.g., user@example.com)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
