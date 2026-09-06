

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .application_response import ApplicationResponse
from .o_auth2scopes import OAuth2Scopes
from .user_response import UserResponse


class OAuth2GetAuthorizationResponse(UniversalBaseModel):
    application: ApplicationResponse
    expires: dt.datetime
    scopes: typing.List[OAuth2Scopes]
    user: typing.Optional[UserResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
