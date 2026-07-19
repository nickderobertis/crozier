

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateMcpServerRequestConfig_Sse(UniversalBaseModel):
    """
    The MCP server configuration updates (Stdio, SSE, or Streamable HTTP)
    """

    mcp_server_type: typing.Literal["sse"] = "sse"
    server_url: typing.Optional[str] = None
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


class UpdateMcpServerRequestConfig_Stdio(UniversalBaseModel):
    """
    The MCP server configuration updates (Stdio, SSE, or Streamable HTTP)
    """

    mcp_server_type: typing.Literal["stdio"] = "stdio"
    command: typing.Optional[str] = None
    args: typing.Optional[typing.List[str]] = None
    env: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateMcpServerRequestConfig_StreamableHttp(UniversalBaseModel):
    """
    The MCP server configuration updates (Stdio, SSE, or Streamable HTTP)
    """

    mcp_server_type: typing.Literal["streamable_http"] = "streamable_http"
    server_url: typing.Optional[str] = None
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


UpdateMcpServerRequestConfig = typing_extensions.Annotated[
    typing.Union[
        UpdateMcpServerRequestConfig_Sse,
        UpdateMcpServerRequestConfig_Stdio,
        UpdateMcpServerRequestConfig_StreamableHttp,
    ],
    pydantic.Field(discriminator="mcp_server_type"),
]
