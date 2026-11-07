

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HyperParameters(UniversalBaseModel):
    """
    The hyper parameter settings used in a fine tune job.
    """

    batch_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The batch size to use for training. The batch size is the number of training examples used to train a single forward and backward pass.
    In general, we've found that larger batch sizes tend to work better for larger datasets.
    The default value as well as the maximum value for this property are specific to a base model.
    """

    learning_rate_multiplier: typing.Optional[float] = pydantic.Field(default=None)
    """
    The learning rate multiplier to use for training. The fine-tuning learning rate is the original learning rate used for pre-training multiplied by this value.
    Larger learning rates tend to perform better with larger batch sizes.
    We recommend experimenting with values in the range 0.02 to 0.2 to see what produces the best results.
    """

    n_epochs: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset.
    """

    prompt_loss_weight: typing.Optional[float] = pydantic.Field(default=None)
    """
    The weight to use for loss on the prompt tokens. This controls how much the model tries to learn to generate the prompt
    (as compared to the completion which always has a weight of 1.0), and can add a stabilizing effect to training when completions are short.
    If prompts are extremely long (relative to completions), it may make sense to reduce this weight so as to avoid over-prioritizing learning the prompt.
    """

    compute_classification_metrics: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A value indicating whether to compute classification metrics.
    If set, we calculate classification-specific metrics such as accuracy and F-1 score using the validation set at the end of every epoch.
    These metrics can be viewed in the results file. In order to compute classification metrics, you must provide a validation_file.Additionally,
    you must specify classification_n_classes for multiclass classification or classification_positive_class for binary classification.
    """

    classification_n_classes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of classes in a classification task.
    This parameter is required for multiclass classification.
    """

    classification_positive_class: typing.Optional[str] = pydantic.Field(default=None)
    """
    The positive class in binary classification.
    This parameter is needed to generate precision, recall, and F1 metrics when doing binary classification.
    """

    classification_betas: typing.Optional[typing.List[float]] = pydantic.Field(default=None)
    """
    The classification beta values. If this is provided, we calculate F-beta scores at the specified beta values.
    The F-beta score is a generalization of F-1 score. This is only used for binary classification.
    With a beta of 1 (i.e.the F-1 score), precision and recall are given the same weight.
    A larger beta score puts more weight on recall and less on precision. A smaller beta score puts more weight on precision and less on recall.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
