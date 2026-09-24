

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .base_mcp_auth_required_event import BaseMcpAuthRequiredEvent
from .mcp_server_auth_info import McpServerAuthInfo


class McpAuthRequiredEvent(BaseMcpAuthRequiredEvent):
    mcp_servers: typing.List[McpServerAuthInfo] = pydantic.Field()
    """
    Servers that need authorization, each with an auth_url.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
