

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_well_known_openid_configuration_response_id_token_signing_alg_values_supported_item import (
    GetWellKnownOpenidConfigurationResponseIdTokenSigningAlgValuesSupportedItem,
)
from .get_well_known_openid_configuration_response_response_modes_supported_item import (
    GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem,
)
from .get_well_known_openid_configuration_response_token_endpoint_auth_signing_alg_values_supported_item import (
    GetWellKnownOpenidConfigurationResponseTokenEndpointAuthSigningAlgValuesSupportedItem,
)


class GetWellKnownOpenidConfigurationResponse(UniversalBaseModel):
    issuer: str = pydantic.Field()
    """
    URL using the https scheme with no query or fragment component that the RP asserts as its Issuer Identifier. This also MUST be identical to the iss Claim value in ID Tokens issued from this Issuer.
    """

    authorization_endpoint: str = pydantic.Field()
    """
    URL of the OAuth 2.0 Authorization Endpoint.
    """

    token_endpoint: str = pydantic.Field()
    """
    URL of the OAuth 2.0 Token Endpoint.
    """

    userinfo_endpoint: str = pydantic.Field()
    """
    URL of the OP's UserInfo Endpoint.
    """

    jwks_uri: str = pydantic.Field()
    """
    URL of the OP's JSON Web Key Set [JWK] document.
    """

    registration_endpoint: str = pydantic.Field()
    """
    URL of Client Registration Endpoint.
    """

    scopes_supported: typing.List[typing.Any] = pydantic.Field()
    """
    JSON array containing a list of the OAuth 2.0 [RFC6749] scope values that this server supports.
    """

    response_types_supported: typing.List[typing.Any] = pydantic.Field()
    """
    JSON array containing a list of the OAuth 2.0 response_type values that this OP supports.
    """

    acr_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    JSON array containing a list of the Authentication Context Class References that IDP supports.
    """

    userinfo_signing_alg_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    JSON array containing a list of the JWS [JWS] signing algorithms.
    """

    userinfo_encryption_alg_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    JSON array containing a list of the JWE [JWE] encryption algorithms.
    """

    userinfo_encryption_enc_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    JSON array containing a list of the JWE encryption algorithms (enc values) [JWA] supported by the UserInfo Endpoint to encode the Claims in a JWT.
    """

    token_endpoint_auth_methods_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    JSON array containing a list of Client Authentication methods supported by this Token Endpoint.
    """

    display_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    JSON array containing a list of the display parameter values that the OpenID Provider supports.
    """

    claim_types_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    JSON array containing a list of the Claim Types that the OpenID Provider supports.
    """

    claims_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for.
    """

    claims_locales_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Languages and scripts supported for values in Claims being returned.
    """

    ui_locales_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Languages and scripts supported for the user interface.
    """

    response_modes_supported: typing.Optional[
        typing.List[GetWellKnownOpenidConfigurationResponseResponseModesSupportedItem]
    ] = pydantic.Field(default=None)
    """
    Mechanism to be used for returning parameters from the Authorization Endpoint.
    """

    token_endpoint_auth_signing_alg_values_supported: typing.Optional[
        typing.List[GetWellKnownOpenidConfigurationResponseTokenEndpointAuthSigningAlgValuesSupportedItem]
    ] = None
    id_token_signing_alg_values_supported: typing.Optional[
        typing.List[GetWellKnownOpenidConfigurationResponseIdTokenSigningAlgValuesSupportedItem]
    ] = None
    verified_claims_supported: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean value indicating support for verified_claims, i.e., the OpenID Connect for Identity Assurance extension.
    """

    claims_in_verified_claims_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    JSON array containing all Claims supported within verified_claims. Claims that are not present in this array MUST NOT be returned within the verified_claims object.
    """

    trust_frameworks_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    JSON array containing all supported trust frameworks.
    """

    evidence_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    JSON array containing all types of identity evidence the OP uses.
    """

    documents_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    JSON array containing all identity document types utilized by the OP for identity verification.
    """

    attachments_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    JSON array containing all attachment types supported by the OP. Possible values are external and embedded.
    """

    digest_algorithms_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    JSON array containing all supported digest algorithms which can be used as alg property within the digest object of external attachments.
    """

    pushed_authorization_request_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the pushed authorization request endpoint at which a client can post an authorization request to exchange for a request_uri value usable at the authorization server.
    """

    require_pushed_authorization_requests: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean parameter indicating whether the authorization server accepts authorization request data only via PAR. If omitted, the default value is false
    """

    dpop_signing_alg_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    JSON array containing a list of the JWS algorithms supported for DPoP proof JWTs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
