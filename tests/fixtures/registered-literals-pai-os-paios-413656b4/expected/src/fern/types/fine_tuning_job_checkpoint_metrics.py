

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FineTuningJobCheckpointMetrics(UniversalBaseModel):
    """
    Metrics at the step number during the fine-tuning job.
    """

    step: typing.Optional[float] = None
    train_loss: typing.Optional[float] = None
    train_mean_token_accuracy: typing.Optional[float] = None
    valid_loss: typing.Optional[float] = None
    valid_mean_token_accuracy: typing.Optional[float] = None
    full_valid_loss: typing.Optional[float] = None
    full_valid_mean_token_accuracy: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
