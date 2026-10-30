

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_event import WebhookEvent
from .webhook_state import WebhookState


class Webhook(UniversalBaseModel):
    """
    The webhook object
    """

    webhook_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of this webhook
    """

    list_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the list to which the field belongs
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    The account timezone used for datetime fields
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of creation
    """

    created_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of creation in ISO format
    """

    modified: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of last modification made
    """

    modified_iso: typing.Optional[str] = pydantic.Field(default=None)
    """
    Date and time of last modification in ISO format
    """

    state: typing.Optional[WebhookState] = pydantic.Field(default=None)
    """
    The status of this webhook: active or deleted
    """

    event: typing.Optional[WebhookEvent] = pydantic.Field(default=None)
    """
    When will the webhook be requested? (subscribed, modified or deactivated)
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL to be accessed
    """

    blocked: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Is the accessing of the webhook (temporarily) blocked? (true or false)
    """

    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    The webhook's signing secret, used to verify that incoming requests are from Laposta (see 'Webhook security' above)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
