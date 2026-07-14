

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_event_logs_filter_service import WebhookEventLogsFilterService


class WebhookEventLogsFilter(UniversalBaseModel):
    consumer_id: typing.Optional[str] = None
    entity_type: typing.Optional[str] = None
    event_type: typing.Optional[str] = None
    exclude_apis: typing.Optional[str] = None
    service: typing.Optional[WebhookEventLogsFilterService] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
