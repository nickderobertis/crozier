

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .list_webhook_events_response_events_item_delivery_status import ListWebhookEventsResponseEventsItemDeliveryStatus
from .list_webhook_events_response_events_item_event_type import ListWebhookEventsResponseEventsItemEventType


class ListWebhookEventsResponseEventsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Event ID
    """

    webhook_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webhookId"),
        pydantic.Field(alias="webhookId", description="Webhook ID"),
    ] = None
    """
    Webhook ID
    """

    webhook_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="webhookUrl"),
        pydantic.Field(alias="webhookUrl", description="The URL the webhook was sent to"),
    ] = None
    """
    The URL the webhook was sent to
    """

    event_type: typing_extensions.Annotated[
        typing.Optional[ListWebhookEventsResponseEventsItemEventType],
        FieldMetadata(alias="eventType"),
        pydantic.Field(alias="eventType", description="Type of event"),
    ] = None
    """
    Type of event
    """

    delivery_status: typing_extensions.Annotated[
        typing.Optional[ListWebhookEventsResponseEventsItemDeliveryStatus],
        FieldMetadata(alias="deliveryStatus"),
        pydantic.Field(alias="deliveryStatus", description="Delivery status of the webhook"),
    ] = None
    """
    Delivery status of the webhook
    """

    status_code: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="statusCode"),
        pydantic.Field(alias="statusCode", description="HTTP status code returned by the webhook endpoint"),
    ] = None
    """
    HTTP status code returned by the webhook endpoint
    """

    response: typing.Optional[str] = pydantic.Field(default=None)
    """
    Response body from the webhook endpoint
    """

    retry: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of retry attempts
    """

    payload: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    The webhook payload that was sent
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="When the event was created"),
    ] = None
    """
    When the event was created
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="When the event was last updated"),
    ] = None
    """
    When the event was last updated
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
