

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fine_tuning_job_checkpoint import FineTuningJobCheckpoint
from .list_fine_tuning_job_checkpoints_response_object import ListFineTuningJobCheckpointsResponseObject


class ListFineTuningJobCheckpointsResponse(UniversalBaseModel):
    data: typing.List[FineTuningJobCheckpoint]
    object: ListFineTuningJobCheckpointsResponseObject
    first_id: typing.Optional[str] = None
    last_id: typing.Optional[str] = None
    has_more: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
