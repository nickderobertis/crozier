

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .error import Error


class CreateMobileAuthorizationCodeResponse(UniversalBaseModel):
    """
    Defines the fields that are included in the response body of
    a request to the __CreateMobileAuthorizationCode__ endpoint.
    """

    authorization_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Generated authorization code that connects a mobile application instance
    to a Square account.
    """

    error: typing.Optional[Error] = None
    expires_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp when `authorization_code` expires in
    [RFC 3339](https://tools.ietf.org/html/rfc3339) format, e.g., "2016-09-04T23:59:33.123Z".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
