

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checksum_algorithm import ChecksumAlgorithm
from .content_ref import ContentRef
from .namespace_id import NamespaceId
from .object_transfer_access import ObjectTransferAccess
from .upload_id import UploadId
from .upload_mode import UploadMode


class UploadSessionStatusOpen(UniversalBaseModel):
    """
    A session that accepts content until its lease ends.
    """

    access: typing.Optional[ObjectTransferAccess] = pydantic.Field(default=None)
    """
    The capability for the direct PUT. It's present for `direct_put` sessions, and the
    server creates a new one on every read.
    """

    checksum_algorithm: ChecksumAlgorithm = pydantic.Field()
    """
    The checksum algorithm that the store uses for content.
    """

    content_ref: typing.Optional[ContentRef] = pydantic.Field(default=None)
    """
    The staged content. It's present after content is staged in a `service_proxied` session.
    """

    expires_at_ms: int = pydantic.Field()
    """
    The time after which cleanup can abort the session, in Unix milliseconds.
    """

    mode: UploadMode = pydantic.Field()
    """
    The transport that was selected when the session began.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the session belongs to.
    """

    part_size_bytes: typing.Optional[int] = pydantic.Field(default=None)
    """
    The size of every part except the last, in bytes. It's present for `direct_multipart`
    sessions.
    """

    upload_id: UploadId = pydantic.Field()
    """
    The upload session ID.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
