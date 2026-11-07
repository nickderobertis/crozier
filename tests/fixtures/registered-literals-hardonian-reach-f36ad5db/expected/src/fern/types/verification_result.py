

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VerificationResult(UniversalBaseModel):
    verified: bool
    name: typing.Optional[str] = None
    signature_valid: typing.Optional[bool] = None
    spec_compatible: typing.Optional[bool] = None
    run_id: typing.Optional[str] = None
    run_fingerprint: typing.Optional[str] = None
    recomputed_fingerprint: typing.Optional[str] = None
    audit_root: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
