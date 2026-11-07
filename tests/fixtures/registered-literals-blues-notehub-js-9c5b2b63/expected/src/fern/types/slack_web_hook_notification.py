

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .slack_web_hook_notification_message_type import SlackWebHookNotificationMessageType


class SlackWebHookNotification(UniversalBaseModel):
    message_type: typing.Optional[SlackWebHookNotificationMessageType] = pydantic.Field(default=None)
    """
    text or blocks
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text of the message, or the blocks definition
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the Slack webhook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
