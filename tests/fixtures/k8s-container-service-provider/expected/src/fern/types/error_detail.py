

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ErrorDetail(UniversalBaseModel):
    """
    Individual validation error within a multi-error response
    """

    detail: str = pydantic.Field()
    """
    Human-readable explanation of this specific validation error
    """

    pointer: typing.Optional[str] = pydantic.Field(default=None)
    """
    JSON Pointer fragment identifier (RFC 6901 §6) locating the request body field that caused this error, e.g. "#/spec/resources/cpu/min". Absent when the error cannot be attributed to a single request body field.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
