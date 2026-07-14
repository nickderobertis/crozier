

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .user_collection_item import UserCollectionItem


class UserCollection(CollectionInfo):
    """
    Collection of users.

    *New in version 2.1.0*
    """

    users: typing.Optional[typing.List[UserCollectionItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
