

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .mcp_server_manifest_auth import McpServerManifestAuth
from .resource_name import ResourceName


class McpServerManifest_Remote(UniversalBaseModel):
    type: typing.Literal["remote"] = "remote"
    auth: typing.Optional[McpServerManifestAuth] = None
    description: str
    name: ResourceName
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class McpServerManifest_Truefoundry(UniversalBaseModel):
    type: typing.Literal["truefoundry"] = "truefoundry"
    auth: typing.Optional[McpServerManifestAuth] = None
    description: str
    name: ResourceName
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


McpServerManifest = typing_extensions.Annotated[
    typing.Union[McpServerManifest_Remote, McpServerManifest_Truefoundry], pydantic.Field(discriminator="type")
]
