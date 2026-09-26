

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_remote_config_oauth import McpRemoteConfigOauth


class McpRemoteConfig(UniversalBaseModel):
    url: str = pydantic.Field()
    """
    URL of the remote MCP server
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable or disable the MCP server on startup
    """

    headers: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Headers to send with the request
    """

    oauth: typing.Optional[McpRemoteConfigOauth] = pydantic.Field(default=None)
    """
    OAuth authentication configuration for the MCP server. Set to false to disable OAuth auto-detection.
    """

    timeout: typing.Optional[int] = pydantic.Field(default=None)
    """
    Timeout in ms for MCP server requests. Defaults to 5000 (5 seconds) if not specified.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
