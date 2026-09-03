

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OidcDiscovery(UniversalBaseModel):
    issuer: str
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: typing.Optional[str] = None
    introspection_endpoint: typing.Optional[str] = None
    jwks_uri: str
    pushed_authorization_request_endpoint: typing.Optional[str] = None
    response_types_supported: typing.List[str]
    response_modes_supported: typing.Optional[typing.List[str]] = None
    grant_types_supported: typing.Optional[typing.List[str]] = None
    subject_types_supported: typing.List[str]
    scopes_supported: typing.Optional[typing.List[str]] = None
    token_endpoint_auth_methods_supported: typing.Optional[typing.List[str]] = None
    token_endpoint_auth_signing_alg_values_supported: typing.Optional[typing.List[str]] = None
    id_token_signing_alg_values_supported: typing.List[str]
    request_object_signing_alg_values_supported: typing.Optional[typing.List[str]] = None
    claims_supported: typing.Optional[typing.List[str]] = None
    code_challenge_methods_supported: typing.Optional[typing.List[str]] = None
    dpop_signing_alg_values_supported: typing.Optional[typing.List[str]] = None
    require_pushed_authorization_requests: typing.Optional[bool] = None
    require_signed_request_object: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
