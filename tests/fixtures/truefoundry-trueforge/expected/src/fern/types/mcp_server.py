

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_approval_tool_selector import McpServerApprovalToolSelector
from .mcp_server_tool_selector import McpServerToolSelector


class McpServer(UniversalBaseModel):
    disable_tools: typing.Optional[typing.List[McpServerToolSelector]] = pydantic.Field(default=None)
    """
    Tools subtracted from the enabled set. Default: none.
    """

    enable_tools: typing.Optional[typing.List[McpServerToolSelector]] = pydantic.Field(default=None)
    """
    Tools exposed to the agent: `@all`, `@read-only`, or literal tool names. Default: `["@all"]`.
    """

    name: str = pydantic.Field()
    """
    Name of a configured MCP server (Settings → Connectors).
    """

    preload: typing.Optional[bool] = pydantic.Field(default=None)
    """
    When true, load all tool schemas upfront. Default: false (deferred discovery).
    """

    preload_tools: typing.Optional[typing.List[McpServerToolSelector]] = pydantic.Field(default=None)
    """
    Tools loaded eagerly into context while the rest stay deferred. A non-empty list implies `preload: false`.
    """

    require_approval_for_tools: typing.Optional[typing.List[McpServerApprovalToolSelector]] = pydantic.Field(
        default=None
    )
    """
    Tools that pause for human approval: `@all`, `@write`, `@destructive`, or literal names. Default: `["@write", "@destructive"]`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
