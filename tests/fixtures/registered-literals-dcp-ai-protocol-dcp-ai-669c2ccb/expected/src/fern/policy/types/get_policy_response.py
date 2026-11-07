

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.verifier_policy import VerifierPolicy


class GetPolicyResponse(UniversalBaseModel):
    policy: typing.Optional[VerifierPolicy] = None
    policy_hash: typing.Optional[str] = None
    mode: typing.Optional[str] = None
    advisory_rejected_algs: typing.Optional[typing.List[str]] = None
    policy_history_length: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
