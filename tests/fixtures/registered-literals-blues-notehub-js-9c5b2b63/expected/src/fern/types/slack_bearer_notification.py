

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .slack_bearer_notification_message_type import SlackBearerNotificationMessageType


class SlackBearerNotification(UniversalBaseModel):
    channel: typing.Optional[str] = pydantic.Field(default=None)
    """
    The channel to send the message to.
    """

    message_type: typing.Optional[SlackBearerNotificationMessageType] = pydantic.Field(default=None)
    """
    text or blocks
    """

    text: typing.Optional[str] = pydantic.Field(default=None)
    """
    The text of the message, or the blocks definition
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The bearer token for the Slack app.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
