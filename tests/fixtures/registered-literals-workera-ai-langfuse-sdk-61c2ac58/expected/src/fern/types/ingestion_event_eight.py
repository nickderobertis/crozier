

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .create_observation_event import CreateObservationEvent
from .ingestion_event_eight_type import IngestionEventEightType


class IngestionEventEight(CreateObservationEvent):
    type: IngestionEventEightType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
