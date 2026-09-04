

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_manifest_auth import McpServerManifestAuth
from .mcp_server_type import McpServerType
from .resource_name import ResourceName


class McpServerManifest(UniversalBaseModel):
    auth: typing.Optional[McpServerManifestAuth] = None
    description: str = pydantic.Field()
    """
    Concise summary of what this MCP server provides.
    """

    name: ResourceName
    type: McpServerType
    url: str = pydantic.Field()
    """
    MCP endpoint URL. For `truefoundry`, the resolved AI Gateway proxy URL.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
