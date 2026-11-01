

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .display_name import DisplayName
from .inode_id import InodeId


class FilesystemOperationCreateDirectoryByInode(UniversalBaseModel):
    """
    An operation that creates a directory under an existing parent inode.
    """

    display_name: DisplayName = pydantic.Field()
    """
    The name of the new directory.
    """

    parent_inode_id: InodeId = pydantic.Field()
    """
    The parent directory.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
