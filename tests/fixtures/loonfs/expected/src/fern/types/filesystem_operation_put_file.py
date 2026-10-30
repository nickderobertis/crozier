

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .content_ref import ContentRef
from .destination_behavior import DestinationBehavior
from .inode_id import InodeId
from .revision_no import RevisionNo


class FilesystemOperationPutFile(UniversalBaseModel):
    """
    An operation that creates or replaces one file from uploaded or inline content.

    The operation requires exactly one of `content_ref` and `inline_content`.
    """

    behavior: typing.Optional[DestinationBehavior] = pydantic.Field(default=None)
    """
    Whether the operation adds a new revision to an existing file or fails with a conflict.
    """

    content_ref: typing.Optional[ContentRef] = pydantic.Field(default=None)
    """
    The uploaded content, which a content token must cover. Set this field or
    `inline_content`, but not both.
    """

    expected_inode_id: typing.Optional[InodeId] = pydantic.Field(default=None)
    """
    The inode that the path must contain. It applies only with `replace` behavior.
    """

    expected_revision_no: typing.Optional[RevisionNo] = pydantic.Field(default=None)
    """
    The content revision that must be the file's current revision. It applies only with
    `replace` behavior and requires `expected_inode_id`.
    """

    inline_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The complete file bytes as base64. Set this field or `content_ref`, but not both.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute destination path. The operation creates any missing ancestor directories.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
