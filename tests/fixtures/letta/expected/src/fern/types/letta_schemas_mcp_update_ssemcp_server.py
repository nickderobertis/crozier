

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LettaSchemasMcpUpdateSsemcpServer(UniversalBaseModel):
    """
    Update an SSE MCP server
    """

    server_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the MCP server
    """

    server_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the server (MCP SSE client will connect to this URL)
    """

    token: typing.Optional[str] = pydantic.Field(default=None)
    """
    The access token or API key for the MCP server (used for SSE authentication)
    """

    custom_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Custom authentication headers as key-value pairs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
