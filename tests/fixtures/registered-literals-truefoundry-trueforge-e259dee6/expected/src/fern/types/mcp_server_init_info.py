

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_init_info_transport_type import McpServerInitInfoTransportType
from .tool_approval_policy_action import ToolApprovalPolicyAction


class McpServerInitInfo(UniversalBaseModel):
    approval_policies: typing.Optional[typing.Dict[str, ToolApprovalPolicyAction]] = pydantic.Field(default=None)
    """
    Sticky per-tool approval policies (keyed by tool name) that auto-allow future calls.
    """

    id: str = pydantic.Field()
    """
    Internal MCP server id.
    """

    name: str = pydantic.Field()
    """
    Configured MCP server name.
    """

    session_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional MCP session id from the transport.
    """

    transport_type: typing.Optional[McpServerInitInfoTransportType] = pydantic.Field(default=None)
    """
    Transport used to connect to the MCP server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
