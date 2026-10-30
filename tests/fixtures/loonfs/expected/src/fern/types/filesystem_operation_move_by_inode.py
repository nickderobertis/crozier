

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .binding_version import BindingVersion
from .destination_behavior import DestinationBehavior
from .display_name import DisplayName
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperationMoveByInode(UniversalBaseModel):
    """
    An operation that moves an inode if its current binding version is
    `expected_binding_version`.
    """

    behavior: typing.Optional[DestinationBehavior] = pydantic.Field(default=None)
    """
    Whether the operation can replace an existing destination file.
    """

    destination_display_name: DisplayName = pydantic.Field()
    """
    The inode's new name.
    """

    destination_parent_inode_id: InodeId = pydantic.Field()
    """
    The destination directory.
    """

    expected_binding_version: BindingVersion = pydantic.Field()
    """
    The binding version that the inode must currently have for the move to succeed.
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
    The inode to move.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
