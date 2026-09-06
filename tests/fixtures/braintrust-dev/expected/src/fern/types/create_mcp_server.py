

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateMcpServer(UniversalBaseModel):
    project_id: str = pydantic.Field()
    """
    Unique identifier for the project that the MCP server belongs under
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
