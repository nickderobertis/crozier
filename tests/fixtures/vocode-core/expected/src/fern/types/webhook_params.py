

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .event_type import EventType
from .http_method import HttpMethod


class WebhookParams(UniversalBaseModel):
    subscriptions: typing.List[EventType]
    url: str
    method: typing.Optional[HttpMethod] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
