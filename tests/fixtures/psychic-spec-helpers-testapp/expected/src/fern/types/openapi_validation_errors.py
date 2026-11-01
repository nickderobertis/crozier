

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .openapi_validation_errors_errors_item import OpenapiValidationErrorsErrorsItem
from .openapi_validation_errors_target import OpenapiValidationErrorsTarget
from .openapi_validation_errors_type import OpenapiValidationErrorsType


class OpenapiValidationErrors(UniversalBaseModel):
    type: OpenapiValidationErrorsType
    target: OpenapiValidationErrorsTarget
    errors: typing.List[OpenapiValidationErrorsErrorsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
