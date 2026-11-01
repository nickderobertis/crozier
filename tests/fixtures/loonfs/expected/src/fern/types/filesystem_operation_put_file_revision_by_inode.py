

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_ref import ContentRef
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperationPutFileRevisionByInode(UniversalBaseModel):
    """
    An operation that adds a revision to a file inode if the inode's current revision is
    `expected_revision_no`.

    The operation requires exactly one of `content_ref` and `inline_content`.
    """

    content_ref: typing.Optional[ContentRef] = pydantic.Field(default=None)
    """
    The uploaded content, which a content token must cover. Set this field or
    `inline_content`, but not both.
    """

    expected_revision_no: RevisionNo = pydantic.Field()
    """
    The revision that must be the file's current revision for the write to succeed.
    """

    inline_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The complete file bytes as base64. Set this field or `content_ref`, but not both.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The file to update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
