

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checksum import Checksum
from .content_id import ContentId
from .content_ref_kind import ContentRefKind
from .namespace_id import NamespaceId


class ContentRef(UniversalBaseModel):
    """
    A reference to a prefix of one content chain, by its owner, content ID, size, and checksum.
    """

    checksum: Checksum = pydantic.Field()
    """
    The required checksum of the referenced bytes.
    """

    content_id: ContentId = pydantic.Field()
    """
    The immutable identity of the content. The content ID and the owner together determine the
    object key.
    """

    kind: ContentRefKind = pydantic.Field()
    """
    The kind of content reference. The format defines one kind, `blob_v1`.
    """

    owner_namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that originally wrote the bytes.
    """

    size_bytes: int = pydantic.Field()
    """
    The length of the referenced bytes, which are a prefix of the content object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
