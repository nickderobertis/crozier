

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateServerResponse(UniversalBaseModel):
    server_url: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="serverUrl"),
        pydantic.Field(
            alias="serverUrl", description="The full URL for connecting to the MCP server, including the instance ID."
        ),
    ]
    """
    The full URL for connecting to the MCP server, including the instance ID.
    """

    instance_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="instanceId"),
        pydantic.Field(
            alias="instanceId",
            description="The unique identifier for this specific server connection integration instance.",
        ),
    ]
    """
    The unique identifier for this specific server connection integration instance.
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
