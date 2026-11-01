

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .destination_behavior import DestinationBehavior
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperationMovePath(UniversalBaseModel):
    """
    An operation that moves a file or directory from one path to another.
    """

    behavior: typing.Optional[DestinationBehavior] = pydantic.Field(default=None)
    """
    Whether the operation can replace an existing destination file.
    """

    destination_path: AbsolutePath = pydantic.Field()
    """
    The absolute destination path. The destination's parent must be visible and writable.
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

    source_path: AbsolutePath = pydantic.Field()
    """
    The absolute source path, which must resolve to a visible inode.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
