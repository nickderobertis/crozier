

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .user_status_private_all_of import UserStatusPrivateAllOf
from .user_status_public import UserStatusPublic


class UserStatusPrivate(UserStatusPublic, UserStatusPrivateAllOf):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
