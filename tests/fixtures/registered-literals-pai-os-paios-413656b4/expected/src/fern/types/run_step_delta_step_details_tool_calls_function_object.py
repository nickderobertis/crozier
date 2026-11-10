

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_delta_step_details_tool_calls_function_object_function import (
    RunStepDeltaStepDetailsToolCallsFunctionObjectFunction,
)


class RunStepDeltaStepDetailsToolCallsFunctionObject(UniversalBaseModel):
    index: int = pydantic.Field()
    """
    The index of the tool call in the tool calls array.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the tool call object.
    """

    function: typing.Optional[RunStepDeltaStepDetailsToolCallsFunctionObjectFunction] = pydantic.Field(default=None)
    """
    The definition of the function that was called.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
