

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .validation_error_error_details_violations_item import ValidationErrorErrorDetailsViolationsItem


class ValidationErrorErrorDetails(UniversalBaseModel):
    """
    Additional error details specific to the error type
    """

    violations: typing.Optional[typing.List[ValidationErrorErrorDetailsViolationsItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
