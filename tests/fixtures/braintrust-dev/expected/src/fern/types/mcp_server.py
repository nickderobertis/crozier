

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class McpServer(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique identifier for the MCP server
    """

    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the MCP server belongs under
    """

    user_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies the user who created the MCP server
    """

    created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of MCP server creation
    """

    deleted_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date of MCP server deletion, or null if the MCP server is still active
    """

    name: str = pydantic.Field()
    """
    Name of the MCP server. Within a project, MCP server names are unique
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Textual description of the MCP server
    """

    url: str = pydantic.Field()
    """
    URL of the MCP server endpoint
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
