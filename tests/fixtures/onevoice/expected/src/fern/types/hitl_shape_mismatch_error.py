

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .hitl_shape_mismatch_error_error import HitlShapeMismatchErrorError


class HitlShapeMismatchError(UniversalBaseModel):
    error: HitlShapeMismatchErrorError
    missing: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
