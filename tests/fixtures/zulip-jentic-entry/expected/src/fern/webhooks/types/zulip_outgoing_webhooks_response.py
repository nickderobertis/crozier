

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .zulip_outgoing_webhooks_response_message import ZulipOutgoingWebhooksResponseMessage


class ZulipOutgoingWebhooksResponse(UniversalBaseModel):
    """
    This is an example of the JSON payload that the Zulip server will `POST`
    to your server:
    """

    bot_email: typing.Optional[str] = pydantic.Field(default=None)
    """
    Email of the bot user.
    """

    bot_full_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The full name of the bot user.
    """

    data: typing.Optional[str] = pydantic.Field(default=None)
    """
    The message content, in raw [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format (not rendered to HTML).
    """

    trigger: typing.Optional[str] = pydantic.Field(default=None)
    """
    What aspect of the message triggered the outgoing webhook notification.
    Possible values include `direct_message` and `mention`.
    
    **Changes**: In Zulip 8.0 (feature level 201), renamed the trigger
    `private_message` to `direct_message`.
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    A string of alphanumeric characters that can be used to authenticate the
    webhook request (each bot user uses a fixed token). You can get the token used by a given outgoing webhook bot
    in the `zuliprc` file downloaded when creating the bot.
    """

    message: typing.Optional[ZulipOutgoingWebhooksResponseMessage] = pydantic.Field(default=None)
    """
    A dictionary containing details on the message that triggered the
    outgoing webhook, in the format used by [`GET /messages`](/api/get-messages).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
