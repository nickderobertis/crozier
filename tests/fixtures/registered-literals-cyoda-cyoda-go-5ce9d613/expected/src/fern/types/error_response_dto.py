

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error_response_dto_error import ErrorResponseDtoError


class ErrorResponseDto(UniversalBaseModel):
    error: ErrorResponseDtoError = pydantic.Field()
    """
    Error codes from RFC 6749 Section 5.2 (OAuth 2.0 Error Response) identifying the type of error
    """

    error_description: str = pydantic.Field()
    """
    Human-readable description of the error
    """

    error_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional URI to documentation about the error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
