

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .inode_id import InodeId
from .revision_no import RevisionNo


class GrepMatch(UniversalBaseModel):
    """
    One match and the line that contains it.
    """

    byte_offset: int = pydantic.Field()
    """
    The match's byte offset within the file.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The matched file's durable inode ID.
    """

    line: str = pydantic.Field()
    """
    The matching line, truncated to the server's maximum line length.
    """

    line_number: int = pydantic.Field()
    """
    The match's line number, counting from 1.
    """

    line_truncated: bool = pydantic.Field()
    """
    Whether the server truncated `line`.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The file's absolute path in the view that the search read.
    """

    revision_no: RevisionNo = pydantic.Field()
    """
    The matched revision, which is the file's newest revision visible to the search.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
