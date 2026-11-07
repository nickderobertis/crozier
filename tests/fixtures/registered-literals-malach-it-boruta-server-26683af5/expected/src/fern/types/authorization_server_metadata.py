

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AuthorizationServerMetadata(UniversalBaseModel):
    issuer: str
    authorization_endpoint: str
    token_endpoint: str
    userinfo_endpoint: typing.Optional[str] = None
    jwks_uri: str
    pushed_authorization_request_endpoint: typing.Optional[str] = None
    credential_issuer: typing.Optional[str] = None
    credential_endpoint: typing.Optional[str] = None
    defered_credential_endpoint: typing.Optional[str] = None
    grant_types_supported: typing.Optional[typing.List[str]] = None
    response_types_supported: typing.Optional[typing.List[str]] = None
    response_modes_supported: typing.Optional[typing.List[str]] = None
    scopes_supported: typing.Optional[typing.List[str]] = None
    subject_types_supported: typing.Optional[typing.List[str]] = None
    token_endpoint_auth_methods_supported: typing.Optional[typing.List[str]] = None
    request_object_signing_alg_values_supported: typing.Optional[typing.List[str]] = None
    id_token_signing_alg_values_supported: typing.Optional[typing.List[str]] = None
    userinfo_signing_alg_values_supported: typing.Optional[typing.List[str]] = None
    credential_configurations_supported: typing.Optional[typing.Dict[str, typing.Any]] = None
    credentials_supported: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
