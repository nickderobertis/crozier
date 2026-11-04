

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .role import Role
from .user import User


class DetailedUser(UniversalBaseModel):
    """
    User detail response with resolved roles.
    """

    roles: typing.List[Role] = pydantic.Field()
    """
    roles granted to the user
    """

    user: User

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
