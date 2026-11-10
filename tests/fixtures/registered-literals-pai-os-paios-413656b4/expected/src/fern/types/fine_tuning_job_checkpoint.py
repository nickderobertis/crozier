

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fine_tuning_job_checkpoint_metrics import FineTuningJobCheckpointMetrics
from .fine_tuning_job_checkpoint_object import FineTuningJobCheckpointObject


class FineTuningJobCheckpoint(UniversalBaseModel):
    """
    The `fine_tuning.job.checkpoint` object represents a model checkpoint for a fine-tuning job that is ready to use.
    """

    id: str = pydantic.Field()
    """
    The checkpoint identifier, which can be referenced in the API endpoints.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the checkpoint was created.
    """

    fine_tuned_model_checkpoint: str = pydantic.Field()
    """
    The name of the fine-tuned checkpoint model that is created.
    """

    step_number: int = pydantic.Field()
    """
    The step number that the checkpoint was created at.
    """

    metrics: FineTuningJobCheckpointMetrics = pydantic.Field()
    """
    Metrics at the step number during the fine-tuning job.
    """

    fine_tuning_job_id: str = pydantic.Field()
    """
    The name of the fine-tuning job that this checkpoint was created from.
    """

    object: FineTuningJobCheckpointObject = pydantic.Field()
    """
    The object type, which is always "fine_tuning.job.checkpoint".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
