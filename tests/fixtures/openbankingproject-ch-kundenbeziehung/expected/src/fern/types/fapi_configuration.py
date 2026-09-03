

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .fapi_configuration_fapi_compliance_level import FapiConfigurationFapiComplianceLevel
from .fapi_configuration_fapi_profile import FapiConfigurationFapiProfile
from .fapi_configuration_fapi_security_profile import FapiConfigurationFapiSecurityProfile


class FapiConfiguration(UniversalBaseModel):
    issuer: str
    fapi_profile: FapiConfigurationFapiProfile
    fapi_security_profile: typing.Optional[FapiConfigurationFapiSecurityProfile] = None
    fapi_compliance_level: typing.Optional[FapiConfigurationFapiComplianceLevel] = None
    require_pushed_authorization_requests: typing.Optional[bool] = None
    require_signed_request_object: typing.Optional[bool] = None
    token_endpoint_auth_methods_supported: typing.Optional[typing.List[str]] = None
    tls_client_certificate_bound_access_tokens: typing.Optional[bool] = None
    dpop_signing_alg_values_supported: typing.Optional[typing.List[str]] = None
    token_binding_methods_supported: typing.Optional[typing.List[str]] = None
    max_authorization_code_lifetime: typing.Optional[int] = None
    max_access_token_lifetime: typing.Optional[int] = None
    max_refresh_token_lifetime: typing.Optional[int] = None
    regulatory_compliance: typing.Optional[typing.List[str]] = None
    supported_use_cases: typing.Optional[typing.List[str]] = None
    swiss_standards_compliance: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
