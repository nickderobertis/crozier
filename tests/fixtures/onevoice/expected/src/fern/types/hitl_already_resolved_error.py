

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hitl_already_resolved_error_error import HitlAlreadyResolvedErrorError
from .hitl_already_resolved_error_reason import HitlAlreadyResolvedErrorReason


class HitlAlreadyResolvedError(UniversalBaseModel):
    error: HitlAlreadyResolvedErrorError
    reason: HitlAlreadyResolvedErrorReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
