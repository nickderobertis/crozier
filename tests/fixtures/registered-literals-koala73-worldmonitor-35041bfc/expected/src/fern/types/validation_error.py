

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field_violation import FieldViolation


class ValidationError(UniversalBaseModel):
    """
    ValidationError is returned when request validation fails. It contains a list of field violations describing what went wrong.
    """

    violations: typing.List[FieldViolation] = pydantic.Field()
    """
    List of validation violations
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
