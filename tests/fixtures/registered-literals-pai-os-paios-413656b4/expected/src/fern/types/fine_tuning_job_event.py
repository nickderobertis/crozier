

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fine_tuning_job_event_level import FineTuningJobEventLevel
from .fine_tuning_job_event_object import FineTuningJobEventObject


class FineTuningJobEvent(UniversalBaseModel):
    """
    Fine-tuning job event object
    """

    id: str
    created_at: int
    level: FineTuningJobEventLevel
    message: str
    object: FineTuningJobEventObject

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
