

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InternalTokenResponse(UniversalBaseModel):
    integration_id: str
    platform: str
    external_id: str
    access_token: str
    user_token: typing.Optional[str] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    expires_at: typing.Optional[dt.datetime] = None
    user_token_expires_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
