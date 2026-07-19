

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FeedsGetMessageResponseMessage(UniversalBaseModel):
    id: str
    feed_id: str
    sequence: float
    content: str
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
