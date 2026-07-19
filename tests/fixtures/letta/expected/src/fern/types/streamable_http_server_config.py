

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_type import McpServerType


class StreamableHttpServerConfig(UniversalBaseModel):
    """
    Configuration for an MCP server using Streamable HTTP
    """

    server_name: str = pydantic.Field()
    """
    The name of the server
    """

    type: typing.Optional[McpServerType] = None
    server_url: str = pydantic.Field()
    """
    The URL of the server
    """

    auth_header: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the authentication header (e.g., 'Authorization')
    """

    auth_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The authentication token or API key value
    """

    custom_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Custom HTTP headers to include with requests
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
