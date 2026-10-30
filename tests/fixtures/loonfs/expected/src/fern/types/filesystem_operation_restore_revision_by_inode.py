

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperationRestoreRevisionByInode(UniversalBaseModel):
    """
    An operation that restores an older revision as the current revision of a file inode.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The visible file to restore.
    """

    source_revision_no: RevisionNo = pydantic.Field()
    """
    An existing older revision. The operation copies its content into a new current
    revision.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
