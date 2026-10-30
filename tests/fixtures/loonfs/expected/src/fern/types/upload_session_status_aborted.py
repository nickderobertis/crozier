

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .namespace_id import NamespaceId
from .upload_id import UploadId
from .upload_mode import UploadMode


class UploadSessionStatusAborted(UniversalBaseModel):
    """
    A session that was aborted before it completed. Its object no longer exists.
    """

    aborted_at_ms: int = pydantic.Field()
    """
    The time the session was aborted, in Unix milliseconds.
    """

    mode: UploadMode = pydantic.Field()
    """
    The transport that was selected when the session began.
    """

    namespace_id: NamespaceId = pydantic.Field()
    """
    The namespace that the session belongs to.
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
