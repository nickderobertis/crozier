

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding import Embedding
from .embeddings_response_model import EmbeddingsResponseModel
from .embeddings_response_object import EmbeddingsResponseObject


class EmbeddingsResponse(UniversalBaseModel):
    object: EmbeddingsResponseObject
    model: EmbeddingsResponseModel
    data: typing.List[Embedding]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
