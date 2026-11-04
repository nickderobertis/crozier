

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .webhook_create_outbound_webhook_response_events_item import WebhookCreateOutboundWebhookResponseEventsItem
from .webhook_create_outbound_webhook_response_scope import WebhookCreateOutboundWebhookResponseScope


class WebhookCreateOutboundWebhookResponse(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)
    """

    verify_tls: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="verify-tls"),
        pydantic.Field(
            alias="verify-tls",
            description="Whether to enforce TLS certificate verification when delivering the webhook",
        ),
    ]
    """
    Whether to enforce TLS certificate verification when delivering the webhook
    """

    id: str = pydantic.Field()
    """
    The unique ID of the webhook
    """

    signing_secret: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="signing-secret"),
        pydantic.Field(
            alias="signing-secret",
            description="Masked value of the secret used to build an HMAC hash of the payload and passed as a header in the webhook request",
        ),
    ]
    """
    Masked value of the secret used to build an HMAC hash of the payload and passed as a header in the webhook request
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updated-at"),
        pydantic.Field(alias="updated-at", description="The date and time the webhook was last updated."),
    ]
    """
    The date and time the webhook was last updated.
    """

    name: str = pydantic.Field()
    """
    Name of the webhook
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="created-at"),
        pydantic.Field(alias="created-at", description="The date and time the webhook was created."),
    ]
    """
    The date and time the webhook was created.
    """

    scope: WebhookCreateOutboundWebhookResponseScope = pydantic.Field()
    """
    The scope in which the relevant events that will trigger webhooks
    """

    events: typing.List[WebhookCreateOutboundWebhookResponseEventsItem] = pydantic.Field()
    """
    Events that will trigger the webhook
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
