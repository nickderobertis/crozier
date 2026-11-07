

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_mcp_server_type import CatalogMcpServerType
from .mcp_server_manifest_auth import McpServerManifestAuth
from .resource_name import ResourceName


class CatalogMcpServer(UniversalBaseModel):
    auth: typing.Optional[McpServerManifestAuth] = None
    description: str = pydantic.Field()
    """
    Concise summary of what this MCP server provides.
    """

    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the MCP server logo asset.
    """

    name: ResourceName
    type: CatalogMcpServerType
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
