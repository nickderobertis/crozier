

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperationAppendFileByInode(UniversalBaseModel):
    """
    An operation that adds bytes to the end of a file inode as its next revision.
    """

    expected_revision_no: typing.Optional[RevisionNo] = pydantic.Field(default=None)
    """
    The content revision that must still be current.
    """

    inline_content: str = pydantic.Field()
    """
    The bytes to add, as base64, from 1 byte to 256 KiB.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The file to append to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
