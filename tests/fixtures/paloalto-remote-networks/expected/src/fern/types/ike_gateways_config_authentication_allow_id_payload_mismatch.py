

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ike_gateways_config_authentication_allow_id_payload_mismatch_local_certificate import (
    IkeGatewaysConfigAuthenticationAllowIdPayloadMismatchLocalCertificate,
)


class IkeGatewaysConfigAuthenticationAllowIdPayloadMismatch(UniversalBaseModel):
    allow_id_payload_mismatch: typing.Optional[bool] = None
    certificate_profile: typing.Optional[str] = None
    local_certificate: typing.Optional[IkeGatewaysConfigAuthenticationAllowIdPayloadMismatchLocalCertificate] = None
    strict_validation_revocation: typing.Optional[bool] = None
    use_management_as_source: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
