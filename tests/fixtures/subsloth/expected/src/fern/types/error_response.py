

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_response_code import ErrorResponseCode
from .error_response_error import ErrorResponseError


class ErrorResponse(UniversalBaseModel):
    """
    Standard error response with message, status code, and optional detail object.
    """

    error: typing.Optional[ErrorResponseError] = None
    message: typing.Optional[str] = None
    status: typing.Optional[int] = None
    code: typing.Optional[ErrorResponseCode] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
