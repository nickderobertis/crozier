

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class McpToolInfo(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Tool name on the MCP server.
    """

    server_id: str = pydantic.Field()
    """
    Internal MCP server id.
    """

    server_name: str = pydantic.Field()
    """
    Configured MCP server name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
