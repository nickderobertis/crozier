

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tool_definition_mode_item import ToolDefinitionModeItem
from .tool_definition_source import ToolDefinitionSource


class ToolDefinition(UniversalBaseModel):
    """
    Tool definition compatible with ai-sdk-ui format.
    """

    description: str
    mode: typing.List[ToolDefinitionModeItem]
    name: str
    parameters: typing.Dict[str, typing.Any]
    source: ToolDefinitionSource

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
