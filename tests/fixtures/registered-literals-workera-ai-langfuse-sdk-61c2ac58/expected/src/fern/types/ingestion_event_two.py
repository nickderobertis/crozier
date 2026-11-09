

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .create_span_event import CreateSpanEvent
from .ingestion_event_two_type import IngestionEventTwoType


class IngestionEventTwo(CreateSpanEvent):
    type: IngestionEventTwoType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
