

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_details_tool_calls_code_object_code_interpreter import RunStepDetailsToolCallsCodeObjectCodeInterpreter


class RunStepDetailsToolCallsCodeObject(UniversalBaseModel):
    """
    Details of the Code Interpreter tool call the run step was involved in.
    """

    id: str = pydantic.Field()
    """
    The ID of the tool call.
    """

    code_interpreter: RunStepDetailsToolCallsCodeObjectCodeInterpreter = pydantic.Field()
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
