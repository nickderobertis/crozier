

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fine_tuning_integration import FineTuningIntegration
from .fine_tuning_job_error import FineTuningJobError
from .fine_tuning_job_hyperparameters import FineTuningJobHyperparameters
from .fine_tuning_job_object import FineTuningJobObject
from .fine_tuning_job_status import FineTuningJobStatus


class FineTuningJob(UniversalBaseModel):
    """
    The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.
    """

    id: str = pydantic.Field()
    """
    The object identifier, which can be referenced in the API endpoints.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the fine-tuning job was created.
    """

    error: typing.Optional[FineTuningJobError] = pydantic.Field(default=None)
    """
    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.
    """

    fine_tuned_model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the fine-tuned model that is being created. The value will be null if the fine-tuning job is still running.
    """

    finished_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the fine-tuning job was finished. The value will be null if the fine-tuning job is still running.
    """

    hyperparameters: FineTuningJobHyperparameters = pydantic.Field()
    """
    The hyperparameters used for the fine-tuning job. See the [fine-tuning guide](/docs/guides/fine-tuning) for more details.
    """

    model: str = pydantic.Field()
    """
    The base model that is being fine-tuned.
    """

    object: FineTuningJobObject = pydantic.Field()
    """
    The object type, which is always "fine_tuning.job".
    """

    organization_id: str = pydantic.Field()
    """
    The organization that owns the fine-tuning job.
    """

    result_files: typing.List[str] = pydantic.Field()
    """
    The compiled results file ID(s) for the fine-tuning job. You can retrieve the results with the [Files API](/docs/api-reference/files/retrieve-contents).
    """

    status: FineTuningJobStatus = pydantic.Field()
    """
    The current status of the fine-tuning job, which can be either `validating_files`, `queued`, `running`, `succeeded`, `failed`, or `cancelled`.
    """

    trained_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The total number of billable tokens processed by this fine-tuning job. The value will be null if the fine-tuning job is still running.
    """

    training_file: str = pydantic.Field()
    """
    The file ID used for training. You can retrieve the training data with the [Files API](/docs/api-reference/files/retrieve-contents).
    """

    validation_file: typing.Optional[str] = pydantic.Field(default=None)
    """
    The file ID used for validation. You can retrieve the validation results with the [Files API](/docs/api-reference/files/retrieve-contents).
    """

    integrations: typing.Optional[typing.List[FineTuningIntegration]] = pydantic.Field(default=None)
    """
    A list of integrations to enable for this fine-tuning job.
    """

    seed: int = pydantic.Field()
    """
    The seed used for the fine-tuning job.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
