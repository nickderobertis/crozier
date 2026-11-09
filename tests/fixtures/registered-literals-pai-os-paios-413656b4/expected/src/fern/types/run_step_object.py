

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_completion_usage import RunStepCompletionUsage
from .run_step_object_last_error import RunStepObjectLastError
from .run_step_object_object import RunStepObjectObject
from .run_step_object_status import RunStepObjectStatus
from .run_step_object_step_details import RunStepObjectStepDetails
from .run_step_object_type import RunStepObjectType


class RunStepObject(UniversalBaseModel):
    """
    Represents a step in execution of a run.
    """

    id: str = pydantic.Field()
    """
    The identifier of the run step, which can be referenced in API endpoints.
    """

    object: RunStepObjectObject = pydantic.Field()
    """
    The object type, which is always `thread.run.step`.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the run step was created.
    """

    assistant_id: str = pydantic.Field()
    """
    The ID of the [assistant](/docs/api-reference/assistants) associated with the run step.
    """

    thread_id: str = pydantic.Field()
    """
    The ID of the [thread](/docs/api-reference/threads) that was run.
    """

    run_id: str = pydantic.Field()
    """
    The ID of the [run](/docs/api-reference/runs) that this run step is a part of.
    """

    type: RunStepObjectType = pydantic.Field()
    """
    The type of run step, which can be either `message_creation` or `tool_calls`.
    """

    status: RunStepObjectStatus = pydantic.Field()
    """
    The status of the run step, which can be either `in_progress`, `cancelled`, `failed`, `completed`, or `expired`.
    """

    step_details: RunStepObjectStepDetails = pydantic.Field()
    """
    The details of the run step.
    """

    last_error: typing.Optional[RunStepObjectLastError] = pydantic.Field(default=None)
    """
    The last error associated with this run step. Will be `null` if there are no errors.
    """

    expired_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run step expired. A step is considered expired if the parent run is expired.
    """

    cancelled_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run step was cancelled.
    """

    failed_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run step failed.
    """

    completed_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run step completed.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    usage: typing.Optional[RunStepCompletionUsage] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
