

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VerificationResult(UniversalBaseModel):
    verified: typing.Optional[bool] = None
    dcp_version: typing.Optional[str] = None
    errors: typing.Optional[typing.List[str]] = None
    warnings: typing.Optional[typing.List[str]] = None
    verifier_policy_hash: typing.Optional[str] = None
    resolved_tier: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
