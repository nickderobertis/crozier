

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .stdio_server_config import StdioServerConfig


class LettaSchemasMcpUpdateStdioMcpServer(UniversalBaseModel):
    """
    Update a Stdio MCP server
    """

    server_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the MCP server
    """

    stdio_config: typing.Optional[StdioServerConfig] = pydantic.Field(default=None)
    """
    The configuration for the server (MCP 'local' client will run this command)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
