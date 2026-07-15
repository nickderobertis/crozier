

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_id import ServiceId
from .webhook_event_type import WebhookEventType


class WebhookEvent(UniversalBaseModel):
    entity_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The service provider's ID of the entity that triggered this event
    """

    entity_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type entity that triggered this event
    """

    entity_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url to retrieve entity detail.
    """

    event_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique reference to this request event
    """

    event_type: typing.Optional[WebhookEventType] = None
    execution_attempt: typing.Optional[float] = pydantic.Field(default=None)
    """
    The current count this request event has been attempted
    """

    occurred_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    ISO Datetime for when the original event occurred
    """

    service_id: typing.Optional[ServiceId] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
