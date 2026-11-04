

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_auth_status import McpAuthStatus
from .mcp_server_manifest import McpServerManifest
from .resource_name import ResourceName


class ConfiguredMcpServer(UniversalBaseModel):
    auth_status: McpAuthStatus
    manifest: McpServerManifest
    name: ResourceName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
