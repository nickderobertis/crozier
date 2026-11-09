

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .create_event_event import CreateEventEvent
from .ingestion_event_six_type import IngestionEventSixType


class IngestionEventSix(CreateEventEvent):
    type: IngestionEventSixType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
