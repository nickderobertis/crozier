

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .verify_bundle_v2response_resolved_tier import VerifyBundleV2ResponseResolvedTier


class VerifyBundleV2Response(UniversalBaseModel):
    verified: typing.Optional[bool] = None
    dcp_version: typing.Optional[str] = None
    errors: typing.Optional[typing.List[str]] = None
    warnings: typing.Optional[typing.List[str]] = None
    verifier_policy_hash: typing.Optional[str] = None
    resolved_tier: typing.Optional[VerifyBundleV2ResponseResolvedTier] = None
    verification_mode: typing.Optional[str] = None
    session_binding_valid: typing.Optional[bool] = None
    manifest_valid: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
