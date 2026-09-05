

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_detail import ErrorDetail
from .error_type import ErrorType


class Error(UniversalBaseModel):
    """
    RFC 9457 compliant error response (Problem Details for HTTP APIs).

    Defined problem types:
    | Type URI | Title | HTTP Status |
    |----------|-------|-------------|
    | .../problems/invalid-argument | Invalid argument | 400 |
    | .../problems/not-found | Not found | 404 |
    | .../problems/already-exists | Already exists | 409 |
    | .../problems/permission-denied | Permission denied | 403 |
    | .../problems/unauthenticated | Unauthenticated | 401 |
    | .../problems/internal | Internal Server Error | 500 |
    | .../problems/unavailable | Service unavailable | 503 |
    """

    type: ErrorType = pydantic.Field()
    """
    URI reference identifying the error type
    """

    title: str = pydantic.Field()
    """
    Short human-readable summary
    """

    status: typing.Optional[int] = pydantic.Field(default=None)
    """
    HTTP status code
    """

    detail: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable explanation specific to this occurrence
    """

    instance: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI reference for this specific error occurrence
    """

    pointer: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSON Pointer fragment identifier (RFC 6901 §6) locating the request body field that caused this error, e.g. "#/spec/resources/cpu/min". Absent when the error cannot be attributed to a single request body field or is not a validation error.
    """

    errors: typing.Optional[typing.List[ErrorDetail]] = pydantic.Field(default=None)
    """
    Present only when two or more same-type validation errors occur.
    Each entry describes one validation failure. Never empty, never
    single-entry. Top-level detail equals the first entry for backward
    compatibility.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
