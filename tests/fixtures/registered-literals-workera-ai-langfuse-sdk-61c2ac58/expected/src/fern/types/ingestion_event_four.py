

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .create_generation_event import CreateGenerationEvent
from .ingestion_event_four_type import IngestionEventFourType


class IngestionEventFour(CreateGenerationEvent):
    type: IngestionEventFourType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
