

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .o_auth_error_error import OAuthErrorError


class OAuthError(UniversalBaseModel):
    error: OAuthErrorError
    error_description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable error description
    """

    error_uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    URI to error documentation
    """

    timestamp: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
