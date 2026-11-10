

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fine_tuning_job_event import FineTuningJobEvent
from .list_fine_tuning_job_events_response_object import ListFineTuningJobEventsResponseObject


class ListFineTuningJobEventsResponse(UniversalBaseModel):
    data: typing.List[FineTuningJobEvent]
    object: ListFineTuningJobEventsResponseObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
