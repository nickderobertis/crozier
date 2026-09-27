

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hitl_reject_reason_too_long_error_error import HitlRejectReasonTooLongErrorError


class HitlRejectReasonTooLongError(UniversalBaseModel):
    error: HitlRejectReasonTooLongErrorError
    max: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
