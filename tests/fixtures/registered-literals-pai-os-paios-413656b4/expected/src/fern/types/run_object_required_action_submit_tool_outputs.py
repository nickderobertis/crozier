

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .run_tool_call_object import RunToolCallObject


class RunObjectRequiredActionSubmitToolOutputs(UniversalBaseModel):
    """
    Details on the tool outputs needed for this run to continue.
    """

    tool_calls: typing.List[RunToolCallObject] = pydantic.Field()
    """
    A list of the relevant tool calls.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
