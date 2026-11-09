

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_tool_call_object_function import RunToolCallObjectFunction
from .run_tool_call_object_type import RunToolCallObjectType


class RunToolCallObject(UniversalBaseModel):
    """
    Tool call objects
    """

    id: str = pydantic.Field()
    """
    The ID of the tool call. This ID must be referenced when you submit the tool outputs in using the [Submit tool outputs to run](/docs/api-reference/runs/submitToolOutputs) endpoint.
    """

    type: RunToolCallObjectType = pydantic.Field()
    """
    The type of tool call the output is required for. For now, this is always `function`.
    """

    function: RunToolCallObjectFunction = pydantic.Field()
    """
    The function definition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
