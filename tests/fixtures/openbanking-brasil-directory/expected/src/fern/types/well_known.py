

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class WellKnown(UniversalBaseModel):
    acr_values_supported: typing.Optional[typing.List[typing.Any]] = None
    authorization_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    REQUIRED. URL of the OP's OAuth 2.0 Authorization Endpoint
    """

    authorization_signing_alg_values_supported: typing.Optional[typing.List[typing.Any]] = None
    check_session_endpoint: typing.Optional[str] = None
    claim_types_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    OPTIONAL. JSON array containing a list of the Claim Types that the OpenID Provider supports
    """

    claims_parameter_supported: typing.Optional[bool] = pydantic.Field(default=None)
    """
    OPTIONAL. Boolean value specifying whether the OP supports use of the claims parameter, with true indicating support. If omitted, the default value is false
    """

    claims_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    RECOMMENDED. JSON array containing a list of the Claim Names of the Claims that the OpenID Provider MAY be able to supply values for
    """

    code_challenge_methods_supported: typing.Optional[typing.List[typing.Any]] = None
    end_session_endpoint: typing.Optional[str] = None
    frontchannel_logout_session_supported: typing.Optional[bool] = None
    frontchannel_logout_supported: typing.Optional[bool] = None
    grant_types_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    OPTIONAL. JSON array containing a list of the OAuth 2.0 Grant Type values that this OP supports
    """

    id_token_signing_alg_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    REQUIRED. JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for the ID Token to encode the Claims in a JWT
    """

    introspection_endpoint: typing.Optional[str] = None
    introspection_endpoint_auth_methods_supported: typing.Optional[typing.List[typing.Any]] = None
    introspection_endpoint_auth_signing_alg_values_supported: typing.Optional[typing.List[typing.Any]] = None
    issuer: typing.Optional[str] = pydantic.Field(default=None)
    """
    REQUIRED. URL using the https scheme with no query or fragment component that the OP asserts as its Issuer Identifier
    """

    jwks_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    REQUIRED. URL of the OP's JSON Web Key Set [JWK] document.
    """

    pushed_authorization_request_endpoint: typing.Optional[typing.List[typing.Any]] = None
    registration_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    RECOMMENDED. URL of the OP's Dynamic Client Registration Endpoint
    """

    request_object_signing_alg_values_supported: typing.Optional[str] = pydantic.Field(default=None)
    """
    OPTIONAL. JSON array containing a list of the JWS signing algorithms (alg values) supported by the OP for Request Objects
    """

    request_parameter_supported: typing.Optional[bool] = pydantic.Field(default=None)
    """
    OPTIONAL. Boolean value specifying whether the OP supports use of the request parameter, with true indicating support. If omitted, the default value is false
    """

    request_uri_parameter_supported: typing.Optional[bool] = pydantic.Field(default=None)
    """
    OPTIONAL. Boolean value specifying whether the OP supports use of the request_uri parameter, with true indicating support. If omitted, the default value is true
    """

    require_request_uri_registration: typing.Optional[bool] = pydantic.Field(default=None)
    """
    OPTIONAL. Boolean value specifying whether the OP requires any request_uri values used to be pre-registered using the request_uris registration parameter
    """

    response_modes_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    OPTIONAL. JSON array containing a list of the OAuth 2.0 response_mode values that this OP supports
    """

    response_types_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    REQUIRED. JSON array containing a list of the OAuth 2.0 response_type values that this OP supports
    """

    revocation_endpoint: typing.Optional[str] = None
    revocation_endpoint_auth_methods_supported: typing.Optional[typing.List[typing.Any]] = None
    revocation_endpoint_auth_signing_alg_values_supported: typing.Optional[typing.List[typing.Any]] = None
    scopes_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    RECOMMENDED. JSON array containing a list of the OAuth 2.0 [RFC6749] scope values that this server supports
    """

    subject_types_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    REQUIRED. JSON array containing a list of the Subject Identifier types that this OP supports
    """

    tls_client_certificate_bound_access_tokens: typing.Optional[bool] = None
    token_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the OP's OAuth 2.0 Token Endpoint
    """

    token_endpoint_auth_methods_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    OPTIONAL. JSON array containing a list of Client Authentication methods supported by this Token Endpoint
    """

    token_endpoint_auth_signing_alg_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(
        default=None
    )
    """
    OPTIONAL. JSON array containing a list of the JWS signing algorithms (alg values) supported by the Token Endpoint for the signature on the JWT
    """

    userinfo_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    RECOMMENDED. URL of the OP's UserInfo Endpoint
    """

    userinfo_signing_alg_values_supported: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    OPTIONAL. JSON array containing a list of the JWS signing algorithms (alg values) [JWA] supported by the UserInfo Endpoint to encode the Claims in a JWT
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
