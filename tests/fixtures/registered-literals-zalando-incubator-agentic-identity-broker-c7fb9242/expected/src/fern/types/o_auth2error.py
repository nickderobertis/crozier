

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .o_auth2error_error import OAuth2ErrorError


class OAuth2Error(UniversalBaseModel):
    error: OAuth2ErrorError = pydantic.Field()
    """
    RFC 8693 error code.
    """

    error_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable error description.
    """

    error_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI directing a user to required broker action, such as re-authentication or the target-agent consent-management page for an impersonation request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
