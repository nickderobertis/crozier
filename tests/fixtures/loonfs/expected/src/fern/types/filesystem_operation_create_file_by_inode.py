

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_ref import ContentRef
from .display_name import DisplayName
from .inode_id import InodeId


class FilesystemOperationCreateFileByInode(UniversalBaseModel):
    """
    An operation that creates a file with an unused name under an existing parent inode.

    The operation requires exactly one of `content_ref` and `inline_content`.
    """

    content_ref: typing.Optional[ContentRef] = pydantic.Field(default=None)
    """
    The uploaded content, which a content token must cover. Set this field or
    `inline_content`, but not both.
    """

    display_name: DisplayName = pydantic.Field()
    """
    The name of the new file.
    """

    inline_content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The complete file bytes as base64. Set this field or `content_ref`, but not both.
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
