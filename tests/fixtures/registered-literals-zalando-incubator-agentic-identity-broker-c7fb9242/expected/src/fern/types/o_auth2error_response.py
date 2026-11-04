

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .o_auth2error_response_error import OAuth2ErrorResponseError


class OAuth2ErrorResponse(UniversalBaseModel):
    error: OAuth2ErrorResponseError = pydantic.Field()
    """
    OAuth2 error code as per RFC 6749.
    Machine-readable code for programmatic error handling.
    """

    error_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional human-readable error description.
    Provides additional context about the error.
    """

    error_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional URI for additional error information.
    Should point to documentation for the error code.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
