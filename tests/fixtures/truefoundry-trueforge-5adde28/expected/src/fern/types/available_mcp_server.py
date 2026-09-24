

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_auth_status import McpAuthStatus
from .mcp_server_auth_public import McpServerAuthPublic
from .resource_name import ResourceName


class AvailableMcpServer(UniversalBaseModel):
    auth: typing.Optional[McpServerAuthPublic] = None
    auth_status: McpAuthStatus
    name: ResourceName
    url: str = pydantic.Field()
    """
    URL of the remote MCP server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
