

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .too_many_requests_response_detail import TooManyRequestsResponseDetail


class TooManyRequestsResponse(UniversalBaseModel):
    detail: typing.Optional[TooManyRequestsResponseDetail] = None
    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    Contains an explanation of the status_code as defined in HTTP/1.1 standard (RFC 6585)
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-readable message providing more details about the error.
    """

    ref: typing.Optional[str] = pydantic.Field(default=None)
    """
    Link to documentation of error type
    """

    status_code: typing.Optional[float] = pydantic.Field(default=None)
    """
    HTTP status code
    """

    type_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of error returned
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
