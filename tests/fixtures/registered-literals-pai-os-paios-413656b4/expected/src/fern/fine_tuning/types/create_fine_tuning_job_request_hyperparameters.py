

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_fine_tuning_job_request_hyperparameters_batch_size import (
    CreateFineTuningJobRequestHyperparametersBatchSize,
)
from .create_fine_tuning_job_request_hyperparameters_learning_rate_multiplier import (
    CreateFineTuningJobRequestHyperparametersLearningRateMultiplier,
)
from .create_fine_tuning_job_request_hyperparameters_n_epochs import CreateFineTuningJobRequestHyperparametersNEpochs


class CreateFineTuningJobRequestHyperparameters(UniversalBaseModel):
    """
    The hyperparameters used for the fine-tuning job.
    """

    batch_size: typing.Optional[CreateFineTuningJobRequestHyperparametersBatchSize] = pydantic.Field(default=None)
    """
    Number of examples in each batch. A larger batch size means that model parameters
    are updated less frequently, but with lower variance.
    """

    learning_rate_multiplier: typing.Optional[CreateFineTuningJobRequestHyperparametersLearningRateMultiplier] = (
        pydantic.Field(default=None)
    )
    """
    Scaling factor for the learning rate. A smaller learning rate may be useful to avoid
    overfitting.
    """

    n_epochs: typing.Optional[CreateFineTuningJobRequestHyperparametersNEpochs] = pydantic.Field(default=None)
    """
    The number of epochs to train the model for. An epoch refers to one full cycle
    through the training dataset.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
