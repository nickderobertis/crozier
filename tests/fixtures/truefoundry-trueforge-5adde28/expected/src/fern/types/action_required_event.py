

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_auth_info import McpServerAuthInfo
from .tool_call_ref import ToolCallRef


class ActionRequiredEvent_McpAuthRequired(UniversalBaseModel):
    type: typing.Literal["mcp.auth_required"] = "mcp.auth_required"
    mcp_servers: typing.List[McpServerAuthInfo]
    created_at: str
    id: str
    thread_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionRequiredEvent_ToolApprovalRequired(UniversalBaseModel):
    type: typing.Literal["tool.approval_required"] = "tool.approval_required"
    created_at: str
    id: str
    thread_id: str
    tool_calls: typing.List[ToolCallRef]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ActionRequiredEvent_ToolResponseRequired(UniversalBaseModel):
    type: typing.Literal["tool.response_required"] = "tool.response_required"
    created_at: str
    id: str
    thread_id: str
    tool_calls: typing.List[ToolCallRef]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ActionRequiredEvent = typing_extensions.Annotated[
    typing.Union[
        ActionRequiredEvent_McpAuthRequired,
        ActionRequiredEvent_ToolApprovalRequired,
        ActionRequiredEvent_ToolResponseRequired,
    ],
    pydantic.Field(discriminator="type"),
]
