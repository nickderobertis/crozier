

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_step_details_tool_calls_code_object_code_interpreter import (
    RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter,
)


class RunStepDeltaStepDetailsToolCallsCodeObject(UniversalBaseModel):
    """
    Details of the Code Interpreter tool call the run step was involved in.
    """

    index: int = pydantic.Field()
    """
    The index of the tool call in the tool calls array.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the tool call.
    """

    code_interpreter: typing.Optional[RunStepDeltaStepDetailsToolCallsCodeObjectCodeInterpreter] = pydantic.Field(
        default=None
    )
    """
    The Code Interpreter tool call definition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
