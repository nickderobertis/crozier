

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_step_details_tool_calls_object_tool_calls_item import (
    RunStepDeltaStepDetailsToolCallsObjectToolCallsItem,
)


class RunStepDeltaStepDetailsToolCallsObject(UniversalBaseModel):
    """
    Details of the tool call.
    """

    tool_calls: typing.Optional[typing.List[RunStepDeltaStepDetailsToolCallsObjectToolCallsItem]] = pydantic.Field(
        default=None
    )
    """
    An array of tool calls the run step was involved in. These can be associated with one of three types of tools: `code_interpreter`, `retrieval`, or `function`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
