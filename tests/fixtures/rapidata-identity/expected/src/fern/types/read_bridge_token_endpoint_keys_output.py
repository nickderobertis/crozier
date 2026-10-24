

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReadBridgeTokenEndpointKeysOutput(UniversalBaseModel):
    access_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="accessToken"),
        pydantic.Field(alias="accessToken", description="The issued access token."),
    ] = None
    """
    The issued access token.
    """

    expires_in: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="expiresIn"),
        pydantic.Field(alias="expiresIn", description="The lifetime of the access token, in seconds."),
    ] = None
    """
    The lifetime of the access token, in seconds.
    """

    refresh_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="refreshToken"),
        pydantic.Field(alias="refreshToken", description="The refresh token used to obtain new access tokens."),
    ] = None
    """
    The refresh token used to obtain new access tokens.
    """

    id_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="idToken"),
        pydantic.Field(alias="idToken", description="The OpenID Connect ID token."),
    ] = None
    """
    The OpenID Connect ID token.
    """

    token_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="tokenType"),
        pydantic.Field(alias="tokenType", description="The type of the issued token."),
    ] = None
    """
    The type of the issued token.
    """

    scope: typing.Optional[str] = pydantic.Field(default=None)
    """
    The scopes granted to the issued token.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
