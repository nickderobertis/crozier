

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .external_server_info import ExternalServerInfo


class StrataAddServersResponse(UniversalBaseModel):
    added_servers: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="addedServers"),
        pydantic.Field(alias="addedServers", description="List of MCP Handle integration that were added"),
    ]
    """
    List of MCP Handle integration that were added
    """

    added_external_servers: typing_extensions.Annotated[
        typing.Optional[typing.List[ExternalServerInfo]],
        FieldMetadata(alias="addedExternalServers"),
        pydantic.Field(
            alias="addedExternalServers", description="List of external MCP servers that were added with name and URL"
        ),
    ] = None
    """
    List of external MCP servers that were added with name and URL
    """

    oauth_urls: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="oauthUrls"),
        pydantic.Field(
            alias="oauthUrls",
            description="Map of connected integration to OAuth URL, supports white labeling if configured",
        ),
    ] = None
    """
    Map of connected integration to OAuth URL, supports white labeling if configured
    """

    api_key_urls: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="apiKeyUrls"),
        pydantic.Field(alias="apiKeyUrls", description="Map of connected integration to API key setup URL"),
    ] = None
    """
    Map of connected integration to API key setup URL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
