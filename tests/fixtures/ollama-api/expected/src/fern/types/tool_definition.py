

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_definition_function import ToolDefinitionFunction
from .tool_definition_type import ToolDefinitionType


class ToolDefinition(UniversalBaseModel):
    type: ToolDefinitionType = pydantic.Field()
    """
    Type of tool (always `function`)
    """

    function: ToolDefinitionFunction

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
