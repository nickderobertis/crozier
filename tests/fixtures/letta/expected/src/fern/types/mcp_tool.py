

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mcp_tool_health import McpToolHealth
from .tool_annotations import ToolAnnotations


class McpTool(UniversalBaseModel):
    """
    A simple wrapper around MCP's tool definition (to avoid conflict with our own)
    """

    name: str
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    input_schema: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="inputSchema"), pydantic.Field(alias="inputSchema")
    ]
    output_schema: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="outputSchema"),
        pydantic.Field(alias="outputSchema"),
    ] = None
    annotations: typing.Optional[ToolAnnotations] = None
    meta: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]], FieldMetadata(alias="_meta"), pydantic.Field(alias="_meta")
    ] = None
    health: typing.Optional[McpToolHealth] = pydantic.Field(default=None)
    """
    Schema health status for OpenAI strict mode
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
