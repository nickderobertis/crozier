

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .external_server_info import ExternalServerInfo


class StrataGetResponse(UniversalBaseModel):
    strata_server_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="strataServerUrl"),
        pydantic.Field(alias="strataServerUrl", description="URL to connect to the Strata MCP server"),
    ]
    """
    URL to connect to the Strata MCP server
    """

    strata_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="strataId"), pydantic.Field(alias="strataId", description="The strata server ID")
    ]
    """
    The strata server ID
    """

    connected_servers: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="connectedServers"),
        pydantic.Field(
            alias="connectedServers", description="List of available integration currently connected to this strata"
        ),
    ]
    """
    List of available integration currently connected to this strata
    """

    connected_external_servers: typing_extensions.Annotated[
        typing.List[ExternalServerInfo],
        FieldMetadata(alias="connectedExternalServers"),
        pydantic.Field(
            alias="connectedExternalServers",
            description="List of external servers with name and URL currently connected to this strata",
        ),
    ]
    """
    List of external servers with name and URL currently connected to this strata
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
