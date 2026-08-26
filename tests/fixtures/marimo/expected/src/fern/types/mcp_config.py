

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .mcp_config_presets_item import McpConfigPresetsItem


class McpConfig(UniversalBaseModel):
    """
    Configuration for MCP servers

    Note: the field name `mcpServers` is camelCased to match MCP server
    config conventions used by popular AI applications (e.g. Cursor, Claude Desktop, etc.)
    """

    mcp_servers: typing_extensions.Annotated[
        typing.Dict[str, typing.Dict[str, typing.Any]],
        FieldMetadata(alias="mcpServers"),
        pydantic.Field(alias="mcpServers"),
    ]
    presets: typing.Optional[typing.List[McpConfigPresetsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
