

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chunk import Chunk
from .chunks_response_model import ChunksResponseModel
from .chunks_response_object import ChunksResponseObject


class ChunksResponse(UniversalBaseModel):
    object: ChunksResponseObject
    model: ChunksResponseModel
    data: typing.List[Chunk]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
