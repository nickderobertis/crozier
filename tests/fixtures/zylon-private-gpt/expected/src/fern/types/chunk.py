

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chunk_object import ChunkObject
from .ingested_doc import IngestedDoc


class Chunk(UniversalBaseModel):
    object: ChunkObject
    score: float
    document: IngestedDoc
    text: str
    previous_texts: typing.Optional[typing.List[str]] = None
    next_texts: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
