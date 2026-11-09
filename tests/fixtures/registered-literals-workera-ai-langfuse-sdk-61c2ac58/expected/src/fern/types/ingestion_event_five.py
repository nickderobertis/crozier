

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .ingestion_event_five_type import IngestionEventFiveType
from .update_generation_event import UpdateGenerationEvent


class IngestionEventFive(UpdateGenerationEvent):
    type: IngestionEventFiveType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
