

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .simple import Simple
from .stream_chunk_inline_nullable import StreamChunkInlineNullable


class StreamChunk(UniversalBaseModel):
    id: str
    inline_nullable: typing.Optional[StreamChunkInlineNullable] = None
    referenced_nullable: typing.Optional[Simple] = None
    required_nullable: typing.Optional[str] = None
    required_referenced_nullable: Simple

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
