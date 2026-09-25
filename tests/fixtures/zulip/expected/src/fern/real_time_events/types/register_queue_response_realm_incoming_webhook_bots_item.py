

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.webhook_config_option import WebhookConfigOption
from ...types.webhook_url_option import WebhookUrlOption


class RegisterQueueResponseRealmIncomingWebhookBotsItem(UniversalBaseModel):
    """
    Object containing details of the bot.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A machine-readable unique name identifying the integration, all-lower-case without
    spaces.
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable display name identifying the integration that this bot implements,
    intended to be used in menus for selecting which integration to create.
    
    **Changes**: New in Zulip 8.0 (feature level 207).
    """

    all_event_types: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    For incoming webhook integrations that support the Zulip server filtering incoming
    events, the list of event types supported by it.
    
    A null value will be present if this incoming webhook integration doesn't support
    such filtering.
    
    **Changes**: New in Zulip 8.0 (feature level 207).
    """

    config_options: typing.Optional[WebhookConfigOption] = None
    url_options: typing.Optional[WebhookUrlOption] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
