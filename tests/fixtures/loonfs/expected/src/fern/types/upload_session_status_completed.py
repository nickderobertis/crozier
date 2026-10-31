

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_ref import ContentRef
from .content_token import ContentToken
from .namespace_id import NamespaceId
from .upload_id import UploadId
from .upload_mode import UploadMode


class UploadSessionStatusCompleted(UniversalBaseModel):
    """
    A session that ended with durable, verified content.
    """

    completed_at_ms: int = pydantic.Field()
    """
    The time the session completed, in Unix milliseconds.
    """

    content_ref: ContentRef = pydantic.Field()
    """
    The verified content that the session completed with.
    """

    content_token: typing.Optional[ContentToken] = pydantic.Field(default=None)
    """
    A new content token, which a later commit can use to reference the content. It's absent
    after the window for issuing tokens closes.
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
