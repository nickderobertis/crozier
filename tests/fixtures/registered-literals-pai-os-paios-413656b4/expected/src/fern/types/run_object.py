

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .assistants_api_response_format_option import AssistantsApiResponseFormatOption
from .assistants_api_tool_choice_option import AssistantsApiToolChoiceOption
from .run_completion_usage import RunCompletionUsage
from .run_object_incomplete_details import RunObjectIncompleteDetails
from .run_object_last_error import RunObjectLastError
from .run_object_object import RunObjectObject
from .run_object_required_action import RunObjectRequiredAction
from .run_object_status import RunObjectStatus
from .run_object_tools_item import RunObjectToolsItem
from .truncation_object import TruncationObject


class RunObject(UniversalBaseModel):
    """
    Represents an execution run on a [thread](/docs/api-reference/threads).
    """

    id: str = pydantic.Field()
    """
    The identifier, which can be referenced in API endpoints.
    """

    object: RunObjectObject = pydantic.Field()
    """
    The object type, which is always `thread.run`.
    """

    created_at: int = pydantic.Field()
    """
    The Unix timestamp (in seconds) for when the run was created.
    """

    thread_id: str = pydantic.Field()
    """
    The ID of the [thread](/docs/api-reference/threads) that was executed on as a part of this run.
    """

    assistant_id: str = pydantic.Field()
    """
    The ID of the [assistant](/docs/api-reference/assistants) used for execution of this run.
    """

    status: RunObjectStatus = pydantic.Field()
    """
    The status of the run, which can be either `queued`, `in_progress`, `requires_action`, `cancelling`, `cancelled`, `failed`, `completed`, or `expired`.
    """

    required_action: typing.Optional[RunObjectRequiredAction] = pydantic.Field(default=None)
    """
    Details on the action required to continue the run. Will be `null` if no action is required.
    """

    last_error: typing.Optional[RunObjectLastError] = pydantic.Field(default=None)
    """
    The last error associated with this run. Will be `null` if there are no errors.
    """

    expires_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run will expire.
    """

    started_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run was started.
    """

    cancelled_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run was cancelled.
    """

    failed_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run failed.
    """

    completed_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    The Unix timestamp (in seconds) for when the run was completed.
    """

    incomplete_details: typing.Optional[RunObjectIncompleteDetails] = pydantic.Field(default=None)
    """
    Details on why the run is incomplete. Will be `null` if the run is not incomplete.
    """

    model: str = pydantic.Field()
    """
    The model that the [assistant](/docs/api-reference/assistants) used for this run.
    """

    instructions: str = pydantic.Field()
    """
    The instructions that the [assistant](/docs/api-reference/assistants) used for this run.
    """

    tools: typing.List[RunObjectToolsItem] = pydantic.Field()
    """
    The list of tools that the [assistant](/docs/api-reference/assistants) used for this run.
    """

    file_ids: typing.List[str] = pydantic.Field()
    """
    The list of [File](/docs/api-reference/files) IDs the [assistant](/docs/api-reference/assistants) used for this run.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.
    """

    usage: typing.Optional[RunCompletionUsage] = None
    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    The sampling temperature used for this run. If not set, defaults to 1.
    """

    max_prompt_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of prompt tokens specified to have been used over the course of the run.
    """

    max_completion_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of completion tokens specified to have been used over the course of the run.
    """

    truncation_strategy: TruncationObject
    tool_choice: AssistantsApiToolChoiceOption
    response_format: AssistantsApiResponseFormatOption

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
