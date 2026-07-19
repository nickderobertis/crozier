

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LettaSchemasMcpServerUpdateStdioMcpServer(UniversalBaseModel):
    """
    Update schema for Stdio MCP server - all fields optional
    """

    command: typing.Optional[str] = pydantic.Field(default=None)
    """
    The command to run (MCP 'local' client will run this command)
    """

    args: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The arguments to pass to the command
    """

    env: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Environment variables to set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
