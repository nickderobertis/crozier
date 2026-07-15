

import datetime as dt
import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConnectionImportDataCredentials(UniversalBaseModel):
    access_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Access token
    """

    expires_in: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of seconds until the token expires. If omitted the token will be queued for refresh.
    """

    issued_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The datetime at which the token was issued. If omitted the token will be queued for refresh.
    """

    refresh_token: str = pydantic.Field()
    """
    The refresh token can be used to obtain a new access token.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
