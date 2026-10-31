

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .binding_version import BindingVersion
from .delete_directory_behavior import DeleteDirectoryBehavior
from .inode_id import InodeId


class FilesystemOperationDeleteByInode(UniversalBaseModel):
    """
    An operation that deletes an inode if its current binding version is
    `expected_binding_version`.
    """

    behavior: typing.Optional[DeleteDirectoryBehavior] = pydantic.Field(default=None)
    """
    Whether the operation can recursively delete a non-empty directory.
    """

    expected_binding_version: BindingVersion = pydantic.Field()
    """
    The binding version that the inode must currently have for the delete to succeed.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The inode to delete.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
