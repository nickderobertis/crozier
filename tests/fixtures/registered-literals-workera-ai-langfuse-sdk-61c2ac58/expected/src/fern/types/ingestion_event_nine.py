

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .ingestion_event_nine_type import IngestionEventNineType
from .update_observation_event import UpdateObservationEvent


class IngestionEventNine(UpdateObservationEvent):
    type: IngestionEventNineType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
