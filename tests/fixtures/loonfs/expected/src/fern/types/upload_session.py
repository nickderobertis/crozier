

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .checksum_algorithm import ChecksumAlgorithm
from .content_ref import ContentRef
from .content_token import ContentToken
from .namespace_id import NamespaceId
from .object_transfer_access import ObjectTransferAccess
from .upload_id import UploadId
from .upload_mode import UploadMode


class UploadSession_Aborted(UniversalBaseModel):
    """
    The current state of one upload session.
    """

    status: typing.Literal["aborted"] = "aborted"
    aborted_at_ms: int
    mode: UploadMode
    namespace_id: NamespaceId
    upload_id: UploadId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UploadSession_Completed(UniversalBaseModel):
    """
    The current state of one upload session.
    """

    status: typing.Literal["completed"] = "completed"
    completed_at_ms: int
    content_ref: ContentRef
    content_token: typing.Optional[ContentToken] = None
    mode: UploadMode
    namespace_id: NamespaceId
    upload_id: UploadId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UploadSession_Open(UniversalBaseModel):
    """
    The current state of one upload session.
    """

    status: typing.Literal["open"] = "open"
    access: typing.Optional[ObjectTransferAccess] = None
    checksum_algorithm: ChecksumAlgorithm
    content_ref: typing.Optional[ContentRef] = None
    expires_at_ms: int
    mode: UploadMode
    namespace_id: NamespaceId
    part_size_bytes: typing.Optional[int] = None
    upload_id: UploadId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UploadSession = typing_extensions.Annotated[
    typing.Union[UploadSession_Aborted, UploadSession_Completed, UploadSession_Open],
    pydantic.Field(discriminator="status"),
]
