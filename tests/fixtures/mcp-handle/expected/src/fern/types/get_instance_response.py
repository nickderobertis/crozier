

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GetInstanceResponse(UniversalBaseModel):
    instance_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="instanceId"),
        pydantic.Field(alias="instanceId", description="The unique identifier of the connection integration instance."),
    ] = None
    """
    The unique identifier of the connection integration instance.
    """

    auth_needed: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="authNeeded"),
        pydantic.Field(
            alias="authNeeded", description="Indicates whether authentication is required for this server instance."
        ),
    ] = None
    """
    Indicates whether authentication is required for this server instance.
    """

    is_authenticated: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="isAuthenticated"),
        pydantic.Field(
            alias="isAuthenticated", description="Indicates whether the instance is authenticated successfully."
        ),
    ] = None
    """
    Indicates whether the instance is authenticated successfully.
    """

    server_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="serverName"),
        pydantic.Field(alias="serverName", description="The name of the MCP server associated with the instance."),
    ] = None
    """
    The name of the MCP server associated with the instance.
    """

    platform: typing.Optional[str] = pydantic.Field(default=None)
    """
    The platform associated with the instance.
    """

    external_user_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="externalUserId"),
        pydantic.Field(alias="externalUserId", description="The user's identifier on the external platform."),
    ] = None
    """
    The user's identifier on the external platform.
    """

    oauth_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="oauthUrl"),
        pydantic.Field(
            alias="oauthUrl",
            description="The OAuth URL for authentication if available, supports white label if configured.",
        ),
    ] = None
    """
    The OAuth URL for authentication if available, supports white label if configured.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
