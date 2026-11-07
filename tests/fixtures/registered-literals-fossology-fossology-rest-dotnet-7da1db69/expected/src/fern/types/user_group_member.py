

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user import User


class UserGroupMember(UniversalBaseModel):
    user: typing.Optional[User] = None
    group_perm: typing.Optional[int] = pydantic.Field(default=None)
    """
    Permission of the user in the group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
