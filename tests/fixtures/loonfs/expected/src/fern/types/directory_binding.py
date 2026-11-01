

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .display_name import DisplayName
from .inode_id import InodeId
from .name_key import NameKey


class DirectoryBinding(UniversalBaseModel):
    """
    A directory entry's parent and name.
    """

    display_name: DisplayName = pydantic.Field()
    """
    The name that users see.
    """

    name_key: NameKey = pydantic.Field()
    """
    The name key that lookups use to find the entry.
    """

    parent_inode_id: InodeId = pydantic.Field()
    """
    The parent directory that contains the entry.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
