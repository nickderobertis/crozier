

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .request_id import RequestId
from .user_id import UserId
from .user_token import UserToken


class UserCreateResponse(UniversalBaseModel):
    """
    UserCreateResponse defines the response schema for `/user/create`
    """

    request_id: RequestId
    user_id: UserId
    user_token: UserToken

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
