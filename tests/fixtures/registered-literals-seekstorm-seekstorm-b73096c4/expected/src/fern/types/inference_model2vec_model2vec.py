

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model import Model
from .quantization import Quantization


class InferenceModel2VecModel2Vec(UniversalBaseModel):
    """
    Predefined model2vec models, already normalized + dot product = cosine similarity, use the same similarity metric that was used during the training of the embedding model.
    """

    model: Model = pydantic.Field()
    """
    Predefined model type for embeddings.
    """

    chunk_size: int = pydantic.Field()
    """
    Chunk size for splitting input text, e.g. 1000 characters. This should be the same chunk size that was used during the training of the embedding model.
    """

    quantization: Quantization = pydantic.Field()
    """
    Quantization method for embeddings.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
