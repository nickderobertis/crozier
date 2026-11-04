

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FieldViolation(UniversalBaseModel):
    """
    FieldViolation describes a single validation error for a specific field.
    """

    field: str = pydantic.Field()
    """
    The field path that failed validation (e.g., 'user.email' for nested fields). For header validation, this will be the header name (e.g., 'X-API-Key')
    """

    description: str = pydantic.Field()
    """
    Human-readable description of the validation violation (e.g., 'must be a valid email address', 'required field missing')
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
