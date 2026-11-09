

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PersonalAccessTokenInfo(UniversalBaseModel):
    description: typing.Optional[str] = None
    expires_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    New expiration timestamp for the personal access token
    """

    name: typing.Optional[str] = None
    suspended: typing.Optional[bool] = pydantic.Field(default=None)
    """
    if true, the token is temporarily suspended
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
