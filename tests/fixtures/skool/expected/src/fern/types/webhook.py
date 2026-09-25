

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .webhook_events_item import WebhookEventsItem


class Webhook(UniversalBaseModel):
    id: typing.Optional[str] = None
    url: typing.Optional[str] = None
    group: typing.Optional[str] = None
    events: typing.Optional[typing.List[WebhookEventsItem]] = None
    created_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
