

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .o_auth2error_error import OAuth2ErrorError


class OAuth2Error(UniversalBaseModel):
    error: OAuth2ErrorError = pydantic.Field()
    """
    RFC 6749 error code.
    """

    error_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable explanation of the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
