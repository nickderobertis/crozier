

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .get_fapi_config_response_mode import GetFapiConfigResponseMode
from .get_fapi_config_response_specs import GetFapiConfigResponseSpecs


class GetFapiConfigResponse(UniversalBaseModel):
    mode: typing.Optional[GetFapiConfigResponseMode] = pydantic.Field(default=None)
    """
    FAPI mode derived from the service's fapiModes. sp=FAPI 2.0 Security Profile, ms=FAPI 2.0 Message Signing, fapi1-advanced/fapi1-baseline=the FAPI 1.0 parts. 'disabled' means no mode is set; 'unknown' means a mode is set that this server does not recognise — the two are deliberately distinct, so an unrecognised profile is never reported as off.
    """

    dpop_enabled: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="dpopEnabled"),
        pydantic.Field(
            alias="dpopEnabled",
            description="The service's dpopNonceRequired flag. NOT 'is DPoP available' — DPoP works without nonces, so false does not mean DPoP is off.",
        ),
    ] = None
    """
    The service's dpopNonceRequired flag. NOT 'is DPoP available' — DPoP works without nonces, so false does not mean DPoP is off.
    """

    supported_token_auth_methods: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="supportedTokenAuthMethods"),
        pydantic.Field(
            alias="supportedTokenAuthMethods",
            description="Client authentication methods the service permits. FAPI 2.0 requires mTLS or private_key_jwt; which one a given client must use is pinned per client, so there is no service-level 'required' method.",
        ),
    ] = None
    """
    Client authentication methods the service permits. FAPI 2.0 requires mTLS or private_key_jwt; which one a given client must use is pinned per client, so there is no service-level 'required' method.
    """

    certificate_bound_access_tokens: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="certificateBoundAccessTokens"),
        pydantic.Field(
            alias="certificateBoundAccessTokens",
            description="The service's tlsClientCertificateBoundAccessTokens flag — mTLS sender-constraining. DPoP binding is a per-client setting and is not reported here.",
        ),
    ] = None
    """
    The service's tlsClientCertificateBoundAccessTokens flag — mTLS sender-constraining. DPoP binding is a per-client setting and is not reported here.
    """

    par_required: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="parRequired"),
        pydantic.Field(alias="parRequired", description="Whether PAR is required"),
    ] = None
    """
    Whether PAR is required
    """

    pkce_required: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="pkceRequired"),
        pydantic.Field(alias="pkceRequired", description="Whether PKCE is required"),
    ] = None
    """
    Whether PKCE is required
    """

    refresh_token_rotation: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="refreshTokenRotation"),
        pydantic.Field(
            alias="refreshTokenRotation",
            description="Whether refresh tokens are rotated. Derived as refreshTokenKept === false: a kept refresh token is one that survives use, i.e. is not rotated.",
        ),
    ] = None
    """
    Whether refresh tokens are rotated. Derived as refreshTokenKept === false: a kept refresh token is one that survives use, i.e. is not rotated.
    """

    scope_required: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="scopeRequired"),
        pydantic.Field(alias="scopeRequired", description="Whether scope parameter is required"),
    ] = None
    """
    Whether scope parameter is required
    """

    cimd_supported: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="cimdSupported"),
        pydantic.Field(
            alias="cimdSupported",
            description="Whether OAuth Client ID Metadata Document (CIMD) is supported. When enabled, clients can use HTTPS URLs as client_id and Authlete auto-fetches metadata from that URL.",
        ),
    ] = None
    """
    Whether OAuth Client ID Metadata Document (CIMD) is supported. When enabled, clients can use HTTPS URLs as client_id and Authlete auto-fetches metadata from that URL.
    """

    specs: typing.Optional[GetFapiConfigResponseSpecs] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
