

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_response_error import ErrorResponseError


class ErrorResponse(UniversalBaseModel):
    """
    The response shape used for all error responses.
    """

    status: int = pydantic.Field()
    """
    The HTTP status code of the error.
    """

    error: ErrorResponseError = pydantic.Field()
    """
    Detailed information about the error that occurred.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
