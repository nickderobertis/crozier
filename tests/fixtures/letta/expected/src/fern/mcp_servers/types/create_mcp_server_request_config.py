

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateMcpServerRequestConfig_Sse(UniversalBaseModel):
    """
    The MCP server configuration (Stdio, SSE, or Streamable HTTP)
    """

    mcp_server_type: typing.Literal["sse"] = "sse"
    server_url: str
    auth_header: typing.Optional[str] = None
    auth_token: typing.Optional[str] = None
    custom_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateMcpServerRequestConfig_Stdio(UniversalBaseModel):
    """
    The MCP server configuration (Stdio, SSE, or Streamable HTTP)
    """

    mcp_server_type: typing.Literal["stdio"] = "stdio"
    command: str
    args: typing.List[str]
    env: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateMcpServerRequestConfig_StreamableHttp(UniversalBaseModel):
    """
    The MCP server configuration (Stdio, SSE, or Streamable HTTP)
    """

    mcp_server_type: typing.Literal["streamable_http"] = "streamable_http"
    server_url: str
    auth_header: typing.Optional[str] = None
    auth_token: typing.Optional[str] = None
    custom_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateMcpServerRequestConfig = typing_extensions.Annotated[
    typing.Union[
        CreateMcpServerRequestConfig_Sse,
        CreateMcpServerRequestConfig_Stdio,
        CreateMcpServerRequestConfig_StreamableHttp,
    ],
    pydantic.Field(discriminator="mcp_server_type"),
]
