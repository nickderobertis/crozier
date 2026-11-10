

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fine_tuning_job_hyperparameters_n_epochs import FineTuningJobHyperparametersNEpochs


class FineTuningJobHyperparameters(UniversalBaseModel):
    """
    The hyperparameters used for the fine-tuning job. See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.
    """

    n_epochs: FineTuningJobHyperparametersNEpochs = pydantic.Field()
    """
    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.
    "auto" decides the optimal number of epochs based on the size of the dataset. If setting the number manually, we support any number between 1 and 50 epochs.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
