

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_location import ErrorLocation


class ErrorDetails(UniversalBaseModel):
    """
    The error details. Required for client-side `4XX` errors.
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    The field that caused the error. If this field is in the body, set this value to the field's JSON pointer value. Required for client-side errors.
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    The value of the field that caused the error.
    """

    location: typing.Optional[ErrorLocation] = None
    issue: str = pydantic.Field()
    """
    The unique, fine-grained application-level error code.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The human-readable description for an issue. The description can change over the lifetime of an API, so clients must not depend on this value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
