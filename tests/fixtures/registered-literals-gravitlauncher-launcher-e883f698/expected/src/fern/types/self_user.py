

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .user import User
from .user_permissions import UserPermissions


class SelfUser(User):
    """
    Extended User returned from /auth/currentuser. Includes the caller's own permissions in addition to all base User fields.
    """

    permissions: typing.Optional[UserPermissions] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
