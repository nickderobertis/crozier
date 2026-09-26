

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class McpLocalConfig(UniversalBaseModel):
    command: typing.List[str] = pydantic.Field()
    """
    Command and arguments to run the MCP server
    """

    environment: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    Environment variables to set when running the MCP server
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable or disable the MCP server on startup
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
