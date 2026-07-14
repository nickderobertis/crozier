

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user import User


class UserList(UniversalBaseModel):
    """
    Users List
    """

    sum: int = pydantic.Field()
    """
    Total sum of items in the list.
    """

    users: typing.List[User] = pydantic.Field()
    """
    List of users.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
