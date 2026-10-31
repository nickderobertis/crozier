

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperationAppendFile(UniversalBaseModel):
    """
    An operation that adds bytes to the end of a file as its next revision.
    """

    expected_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the path must still resolve to.
    """

    expected_revision_no: typing.Optional[RevisionNo] = pydantic.Field(default=None)
    """
    The content revision that must still be current. It requires `expected_inode_id`.
    """

    inline_content: str = pydantic.Field()
    """
    The bytes to add, as base64, from 1 byte to 256 KiB.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path, which must resolve to a visible file.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
