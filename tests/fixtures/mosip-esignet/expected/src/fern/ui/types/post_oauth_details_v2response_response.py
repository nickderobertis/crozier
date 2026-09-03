

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.auth_factor import AuthFactor


class PostOauthDetailsV2ResponseResponse(UniversalBaseModel):
    transaction_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="transactionId"),
        pydantic.Field(
            alias="transactionId",
            description="This value is passed through unmodified from the /oauth-details request to the /auth-code request.",
        ),
    ]
    """
    This value is passed through unmodified from the /oauth-details request to the /auth-code request.
    """

    auth_factors: typing_extensions.Annotated[
        typing.List[typing.List[AuthFactor]],
        FieldMetadata(alias="authFactors"),
        pydantic.Field(
            alias="authFactors",
            description="Auth factors defines the authentication screens displayed in IDP frontend.\nMore than one authFactor may be resolved or combination of auth factors.\nPrecedence of authFactors is based on its order",
        ),
    ]
    """
    Auth factors defines the authentication screens displayed in IDP frontend.
    More than one authFactor may be resolved or combination of auth factors.
    Precedence of authFactors is based on its order
    """

    essential_claims: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="essentialClaims"),
        pydantic.Field(alias="essentialClaims", description="Array holds all the requested essential claims."),
    ]
    """
    Array holds all the requested essential claims.
    """

    voluntary_claims: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="voluntaryClaims"),
        pydantic.Field(alias="voluntaryClaims", description="Array holds all the requested optional claims."),
    ] = None
    """
    Array holds all the requested optional claims.
    """

    authorize_scopes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="authorizeScopes"),
        pydantic.Field(alias="authorizeScopes", description="Scopes to be permitted by the end user."),
    ] = None
    """
    Scopes to be permitted by the end user.
    """

    configs: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    UI configuration key-value pairs.
    """

    client_name: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="clientName"),
        pydantic.Field(
            alias="clientName",
            description="OIDC client name in different languages where language is the key and client name\nis the value. Default name is passed in @none key.",
        ),
    ] = None
    """
    OIDC client name in different languages where language is the key and client name
    is the value. Default name is passed in @none key.
    """

    logo_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="logoUrl"),
        pydantic.Field(alias="logoUrl", description="Registered OIDC client logo URL."),
    ] = None
    """
    Registered OIDC client logo URL.
    """

    credential_scopes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="credentialScopes"),
        pydantic.Field(alias="credentialScopes", description="List of valid credential scopes requested"),
    ] = None
    """
    List of valid credential scopes requested
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
