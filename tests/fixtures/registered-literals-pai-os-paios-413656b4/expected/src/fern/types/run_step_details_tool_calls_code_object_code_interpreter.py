

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_details_tool_calls_code_object_code_interpreter_outputs_item import (
    RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem,
)


class RunStepDetailsToolCallsCodeObjectCodeInterpreter(UniversalBaseModel):
    """
    The Code Interpreter tool call definition.
    """

    input: str = pydantic.Field()
    """
    The input to the Code Interpreter tool call.
    """

    outputs: typing.List[RunStepDetailsToolCallsCodeObjectCodeInterpreterOutputsItem] = pydantic.Field()
    """
    The outputs from the Code Interpreter tool call. Code Interpreter can output one or more items, including text (`logs`) or images (`image`). Each of these are represented by a different object type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
