

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .track_journey_event_response_meta import TrackJourneyEventResponseMeta


class TrackJourneyEventResponse(UniversalBaseModel):
    meta: TrackJourneyEventResponseMeta
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
