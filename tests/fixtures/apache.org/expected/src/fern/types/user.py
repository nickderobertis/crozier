

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .user_collection_item import UserCollectionItem


class User(UserCollectionItem):
    """
    A user object with sensitive data.

    *New in version 2.1.0*
    """

    password: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
