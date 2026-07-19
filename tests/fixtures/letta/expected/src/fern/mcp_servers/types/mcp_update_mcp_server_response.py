

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class McpUpdateMcpServerResponse_Stdio(UniversalBaseModel):
    mcp_server_type: typing.Literal["stdio"] = "stdio"
    command: str
    args: typing.List[str]
    env: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    id: typing.Optional[str] = None
    server_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpUpdateMcpServerResponse_Sse(UniversalBaseModel):
    mcp_server_type: typing.Literal["sse"] = "sse"
    server_url: str
    auth_header: typing.Optional[str] = None
    auth_token: typing.Optional[str] = None
    custom_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    id: typing.Optional[str] = None
    server_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpUpdateMcpServerResponse_StreamableHttp(UniversalBaseModel):
    mcp_server_type: typing.Literal["streamable_http"] = "streamable_http"
    server_url: str
    auth_header: typing.Optional[str] = None
    auth_token: typing.Optional[str] = None
    custom_headers: typing.Optional[typing.Dict[str, typing.Optional[str]]] = None
    id: typing.Optional[str] = None
    server_name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


McpUpdateMcpServerResponse = typing_extensions.Annotated[
    typing.Union[
        McpUpdateMcpServerResponse_Stdio, McpUpdateMcpServerResponse_Sse, McpUpdateMcpServerResponse_StreamableHttp
    ],
    pydantic.Field(discriminator="mcp_server_type"),
]
