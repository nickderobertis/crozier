

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_ref import ContentRef
from .download_range import DownloadRange
from .inode_id import InodeId
from .namespace_id import NamespaceId
from .revision_no import RevisionNo


class CreateDownloadByInodeResponse(UniversalBaseModel):
    """
    A short-lived capability to read one revision of an inode.
    """

    content_ref: ContentRef = pydantic.Field()
    """
    The content's identity, size, and checksum.
    """

    inode_id: InodeId = pydantic.Field()
    """
    The file inode being read.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that was read.
    """

    ranges: typing.List[DownloadRange] = pydantic.Field()
    """
    The ranges that cover the revision's bytes from the requested offset, in order.
    """

    revision_no: RevisionNo = pydantic.Field()
    """
    The revision being read.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
