

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .collection_info import CollectionInfo
from .role import Role


class RoleCollection(CollectionInfo):
    """
    A collection of roles.

    *New in version 2.1.0*
    """

    roles: typing.Optional[typing.List[Role]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
