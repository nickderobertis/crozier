

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .destination_behavior import DestinationBehavior
from .display_name import DisplayName
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperationCopyByInode(UniversalBaseModel):
    """
    An operation that copies a file inode to a new name under a parent inode.
    """

    behavior: typing.Optional[DestinationBehavior] = pydantic.Field(default=None)
    """
    Whether the operation can replace an existing destination file.
    """

    destination_display_name: DisplayName = pydantic.Field()
    """
    The name of the copy.
    """

    destination_parent_inode_id: InodeId = pydantic.Field()
    """
    The destination directory.
    """

    expected_destination_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the destination path must contain. It applies only with `replace` behavior.
    """

    expected_destination_revision_no: typing.Optional[RevisionNo] = pydantic.Field(default=None)
    """
    The content revision that must be the destination file's current revision. It applies only
    with `replace` behavior and requires `expected_destination_inode_id`.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The file to copy.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
