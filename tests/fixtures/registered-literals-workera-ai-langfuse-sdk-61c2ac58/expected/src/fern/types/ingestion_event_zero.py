

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .ingestion_event_zero_type import IngestionEventZeroType
from .trace_event import TraceEvent


class IngestionEventZero(TraceEvent):
    type: IngestionEventZeroType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
