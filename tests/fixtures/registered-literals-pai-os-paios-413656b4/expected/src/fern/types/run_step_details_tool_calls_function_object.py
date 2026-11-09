

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_step_details_tool_calls_function_object_function import RunStepDetailsToolCallsFunctionObjectFunction


class RunStepDetailsToolCallsFunctionObject(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    The ID of the tool call object.
    """

    function: RunStepDetailsToolCallsFunctionObjectFunction = pydantic.Field()
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
