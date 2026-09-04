

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .post_client_request_request_auth_context_refs_item import PostClientRequestRequestAuthContextRefsItem
from .post_client_request_request_client_auth_methods_item import PostClientRequestRequestClientAuthMethodsItem
from .post_client_request_request_grant_types_item import PostClientRequestRequestGrantTypesItem
from .post_client_request_request_user_claims_item import PostClientRequestRequestUserClaimsItem


class PostClientRequestRequest(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientId"),
        pydantic.Field(
            alias="clientId",
            description="Unique OIDC client id (Case-Sensitive). If duplicates found, request will be rejected.",
        ),
    ]
    """
    Unique OIDC client id (Case-Sensitive). If duplicates found, request will be rejected.
    """

    client_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="clientName"), pydantic.Field(alias="clientName", description="Name of OIDC client.")
    ]
    """
    Name of OIDC client.
    """

    relying_party_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="relyingPartyId"),
        pydantic.Field(
            alias="relyingPartyId",
            description="Relying Party ID of the client. This will be passed on to authentications servers when KYC is fetched.\n\nNote: Use the client Id as relyingPartyId if there is no separate concept of relying party in the ID authentication system.",
        ),
    ]
    """
    Relying Party ID of the client. This will be passed on to authentications servers when KYC is fetched.
    
    Note: Use the client Id as relyingPartyId if there is no separate concept of relying party in the ID authentication system.
    """

    logo_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="logoUri"),
        pydantic.Field(
            alias="logoUri",
            description="Relying party logo URI which will used to display logo in OIDC login and consent pages.",
        ),
    ]
    """
    Relying party logo URI which will used to display logo in OIDC login and consent pages.
    """

    redirect_uris: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="redirectUris"),
        pydantic.Field(
            alias="redirectUris",
            description="Valid list of callback Uris of the relying party. \nWhen OIDC authorize API is called, any one Uri from this list should be sent as redirect_uri. authorization_code will be redirected to this Uri on successful authentication.",
        ),
    ] = None
    """
    Valid list of callback Uris of the relying party. 
    When OIDC authorize API is called, any one Uri from this list should be sent as redirect_uri. authorization_code will be redirected to this Uri on successful authentication.
    """

    auth_context_refs: typing_extensions.Annotated[
        typing.List[PostClientRequestRequestAuthContextRefsItem],
        FieldMetadata(alias="authContextRefs"),
        pydantic.Field(
            alias="authContextRefs",
            description="The Authentication Context Class Reference is case-sensitive string specifying a list of Authentication Context Class values that identifies the Authentication Context Class. Values that the authentication performed satisfied implying a Level Of Assurance.",
        ),
    ]
    """
    The Authentication Context Class Reference is case-sensitive string specifying a list of Authentication Context Class values that identifies the Authentication Context Class. Values that the authentication performed satisfied implying a Level Of Assurance.
    """

    public_key: typing_extensions.Annotated[
        typing.Dict[str, typing.Any],
        FieldMetadata(alias="publicKey"),
        pydantic.Field(
            alias="publicKey",
            description="OIDC client's public key used to verify the client's private_key_jwt when OIDC token endpoint is invoked. \nThis field will not be allowed to udpate later, if the private key is compromised, then new OIDC client to be created.\nFormat : Json Web Key (JWK).",
        ),
    ]
    """
    OIDC client's public key used to verify the client's private_key_jwt when OIDC token endpoint is invoked. 
    This field will not be allowed to udpate later, if the private key is compromised, then new OIDC client to be created.
    Format : Json Web Key (JWK).
    """

    user_claims: typing_extensions.Annotated[
        typing.List[PostClientRequestRequestUserClaimsItem],
        FieldMetadata(alias="userClaims"),
        pydantic.Field(
            alias="userClaims",
            description="Allowed user info claims, that can be requested by OIDC client in the authorize API",
        ),
    ]
    """
    Allowed user info claims, that can be requested by OIDC client in the authorize API
    """

    grant_types: typing_extensions.Annotated[
        typing.List[PostClientRequestRequestGrantTypesItem],
        FieldMetadata(alias="grantTypes"),
        pydantic.Field(alias="grantTypes", description="Form of Authorization Grant presented to token endpoint"),
    ]
    """
    Form of Authorization Grant presented to token endpoint
    """

    client_auth_methods: typing_extensions.Annotated[
        typing.List[PostClientRequestRequestClientAuthMethodsItem],
        FieldMetadata(alias="clientAuthMethods"),
        pydantic.Field(
            alias="clientAuthMethods",
            description='Auth method supported for token endpoint. At present only "private_key_jwt" is supported.',
        ),
    ]
    """
    Auth method supported for token endpoint. At present only "private_key_jwt" is supported.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
