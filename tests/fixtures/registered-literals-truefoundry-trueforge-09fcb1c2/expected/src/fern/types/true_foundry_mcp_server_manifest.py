

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_manifest_auth import McpServerManifestAuth
from .resource_name import ResourceName


class TrueFoundryMcpServerManifest(UniversalBaseModel):
    auth: typing.Optional[McpServerManifestAuth] = None
    description: str = pydantic.Field()
    """
    Concise summary of what this MCP server provides.
    """

    name: ResourceName
    url: str = pydantic.Field()
    """
    Resolved AI Gateway proxy URL for this TrueFoundry-managed MCP server.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
