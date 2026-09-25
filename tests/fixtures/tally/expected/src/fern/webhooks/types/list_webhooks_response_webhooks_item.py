

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.event_type import EventType
from .list_webhooks_response_webhooks_item_http_headers_item import ListWebhooksResponseWebhooksItemHttpHeadersItem


class ListWebhooksResponseWebhooksItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Webhook ID
    """

    form_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="formId"),
        pydantic.Field(alias="formId", description="Form ID the webhook is attached to"),
    ] = None
    """
    Form ID the webhook is attached to
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The webhook endpoint URL
    """

    signing_secret: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="signingSecret"),
        pydantic.Field(alias="signingSecret", description="Secret used to sign webhook payloads"),
    ] = None
    """
    Secret used to sign webhook payloads
    """

    http_headers: typing_extensions.Annotated[
        typing.Optional[typing.List[ListWebhooksResponseWebhooksItemHttpHeadersItem]],
        FieldMetadata(alias="httpHeaders"),
        pydantic.Field(alias="httpHeaders", description="Custom HTTP headers to include in webhook requests"),
    ] = None
    """
    Custom HTTP headers to include in webhook requests
    """

    event_types: typing_extensions.Annotated[
        typing.Optional[typing.List[EventType]],
        FieldMetadata(alias="eventTypes"),
        pydantic.Field(alias="eventTypes", description="Types of events this webhook subscribes to"),
    ] = None
    """
    Types of events this webhook subscribes to
    """

    external_subscriber: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="externalSubscriber"),
        pydantic.Field(alias="externalSubscriber", description="External subscriber identifier"),
    ] = None
    """
    External subscriber identifier
    """

    is_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isEnabled"),
        pydantic.Field(alias="isEnabled", description="Whether the webhook is enabled"),
    ] = None
    """
    Whether the webhook is enabled
    """

    last_synced_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastSyncedAt"),
        pydantic.Field(alias="lastSyncedAt", description="When the webhook was last synced"),
    ] = None
    """
    When the webhook was last synced
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the webhook was created"),
    ] = None
    """
    When the webhook was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="When the webhook was last updated"),
    ] = None
    """
    When the webhook was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
