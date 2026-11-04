

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OAuth2MetadataResponse(UniversalBaseModel):
    issuer: str = pydantic.Field()
    """
    The issuer identifier (this authorization server).
    Must be an HTTPS URI with no query or fragment.
    """

    authorization_endpoint: str = pydantic.Field()
    """
    URL of the authorization endpoint
    """

    token_endpoint: str = pydantic.Field()
    """
    URL of the token endpoint
    """

    userinfo_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the userinfo endpoint (if supported)
    """

    jwks_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the JWKS endpoint (if supported)
    """

    registration_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the dynamic client registration endpoint (if supported)
    """

    response_types_supported: typing.List[str] = pydantic.Field()
    """
    OAuth2 response types supported by this server
    """

    response_modes_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Response modes supported
    """

    grant_types_supported: typing.List[str] = pydantic.Field()
    """
    Grant types supported by this server
    """

    token_endpoint_auth_methods_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Token endpoint authentication methods supported
    """

    token_endpoint_auth_signing_alg_values_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Signing algorithms for client authentication
    """

    service_documentation: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of service documentation
    """

    ui_locales_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    UI locales supported
    """

    op_policy_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of operator policy
    """

    op_tos_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of operator terms of service
    """

    revocation_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Token revocation endpoint URL (if supported)
    """

    introspection_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Token introspection endpoint URL (if supported)
    """

    code_challenge_methods_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    PKCE code challenge methods supported by this server.
    RFC 7636 compliance.
    """

    scopes_supported: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Scopes supported by this server
    """

    client_id_metadata_document_supported: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether this authorization server supports URL-based client_id values
    via the Client ID Metadata Document specification
    (draft-ietf-oauth-client-id-metadata-document-01).
    Present and true when CIMD is enabled; absent when disabled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
