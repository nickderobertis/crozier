

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CreateSelfHostedServerResponse(UniversalBaseModel):
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
            description="The OAuth authorization URL for the specified server, if OAuth is configured.",
        ),
    ] = None
    """
    The OAuth authorization URL for the specified server, if OAuth is configured.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
