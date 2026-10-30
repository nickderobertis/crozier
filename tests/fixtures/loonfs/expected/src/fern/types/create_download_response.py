

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .absolute_path import AbsolutePath
from .content_ref import ContentRef
from .download_range import DownloadRange
from .namespace_id import NamespaceId
from .revision_no import RevisionNo


class CreateDownloadResponse(UniversalBaseModel):
    """
    The signed object ranges for one revision.
    """

    content_ref: ContentRef = pydantic.Field()
    """
    The identity, byte length, and checksum of the revision's bytes.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that was read.
    """

    path: AbsolutePath = pydantic.Field()
    """
    The absolute path, built from the stored display names.
    """

    ranges: typing.List[DownloadRange] = pydantic.Field()
    """
    The ranges that cover the revision's bytes from the requested offset, in order.
    """

    revision_no: RevisionNo = pydantic.Field()
    """
    The revision that the capability reads, as resolved from the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
