

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FeedsListMessagesResponseMessagesItem(UniversalBaseModel):
    id: str
    feed_id: str
    sequence: float
    content_preview: str
    is_truncated: bool
    content_size_bytes: float
    expires_at: str
    created_at: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
