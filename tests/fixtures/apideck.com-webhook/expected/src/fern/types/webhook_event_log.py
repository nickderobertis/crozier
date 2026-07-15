

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_id import ApplicationId
from .consumer_id import ConsumerId
from .unified_api_id import UnifiedApiId
from .webhook_event_log_attempts_item import WebhookEventLogAttemptsItem
from .webhook_event_log_service import WebhookEventLogService


class WebhookEventLog(UniversalBaseModel):
    application_id: typing.Optional[ApplicationId] = None
    attempts: typing.Optional[typing.List[WebhookEventLogAttemptsItem]] = pydantic.Field(default=None)
    """
    record of each attempt to call webhook endpoint
    """

    consumer_id: typing.Optional[ConsumerId] = None
    endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the webhook endpoint.
    """

    entity_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the Entity described by the attributes delivered within payload
    """

    event_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of source event that webhook is subscribed to.
    """

    execution_attempt: typing.Optional[float] = pydantic.Field(default=None)
    """
    Number of attempts webhook endpoint was called before a success was returned or eventually failed
    """

    http_method: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTP Method of request to endpoint.
    """

    id: typing.Optional[str] = None
    request_body: typing.Optional[str] = pydantic.Field(default=None)
    """
    The JSON stringified payload that was delivered to the webhook endpoint.
    """

    response_body: typing.Optional[str] = pydantic.Field(default=None)
    """
    The JSON stringified response that was returned from the webhook endpoint.
    """

    retry_scheduled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    If the request has not hit the max retry limit and will be retried.
    """

    service: typing.Optional[WebhookEventLogService] = pydantic.Field(default=None)
    """
    Apideck service provider associated with event.
    """

    status_code: typing.Optional[int] = pydantic.Field(default=None)
    """
    HTTP Status code that was returned.
    """

    success: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether or not the request was successful.
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO Date and time when the request was made.
    """

    unified_api: typing.Optional[UnifiedApiId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
