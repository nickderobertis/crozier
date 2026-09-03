

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.auth_factor import AuthFactor


class PostAuthorizationLinkTransactionV2ResponseResponse(UniversalBaseModel):
    link_transaction_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="linkTransactionId"),
        pydantic.Field(alias="linkTransactionId", description="Unique link-transaction-id."),
    ] = None
    """
    Unique link-transaction-id.
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
        pydantic.Field(alias="logoUrl", description="Registered OIDC client Logo URL."),
    ] = None
    """
    Registered OIDC client Logo URL.
    """

    authorize_scopes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="authorizeScopes"),
        pydantic.Field(
            alias="authorizeScopes", description="List of requested scopes to be permitted by the end user."
        ),
    ] = None
    """
    List of requested scopes to be permitted by the end user.
    """

    essential_claims: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="essentialClaims"),
        pydantic.Field(alias="essentialClaims", description="List of client request mandatory claim names."),
    ] = None
    """
    List of client request mandatory claim names.
    """

    voluntary_claims: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="voluntaryClaims"),
        pydantic.Field(alias="voluntaryClaims", description="List of client request optional claim names."),
    ] = None
    """
    List of client request optional claim names.
    """

    auth_factors: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.List[AuthFactor]]],
        FieldMetadata(alias="authFactors"),
        pydantic.Field(
            alias="authFactors",
            description="Auth factors defines the authentication screens displayed in IDP frontend. More than one authFactor may be resolved or combination of auth factors. Precedence of authFactors is based on its order",
        ),
    ] = None
    """
    Auth factors defines the authentication screens displayed in IDP frontend. More than one authFactor may be resolved or combination of auth factors. Precedence of authFactors is based on its order
    """

    configs: typing.Optional[typing.Dict[str, typing.Any]] = None
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
