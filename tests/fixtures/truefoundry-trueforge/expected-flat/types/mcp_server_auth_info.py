

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class McpServerAuthInfo(UniversalBaseModel):
    auth_url: str = pydantic.Field()
    """
    URL the user must visit to complete OAuth for this server.
    """

    id: str = pydantic.Field()
    """
    Internal MCP server id.
    """

    name: str = pydantic.Field()
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
