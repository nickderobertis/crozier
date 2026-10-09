

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_auth_status_status import McpAuthStatusStatus


class McpAuthStatus(UniversalBaseModel):
    """
    Current auth state.
    """

    authorization_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    When auth is required, this contains the URL to redirect the user to for authorization.
    """

    status: McpAuthStatusStatus = pydantic.Field()
    """
    Current auth state for this MCP server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
