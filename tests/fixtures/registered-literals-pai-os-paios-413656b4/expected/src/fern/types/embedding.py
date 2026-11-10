

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding_object import EmbeddingObject


class Embedding(UniversalBaseModel):
    """
    Represents an embedding vector returned by embedding endpoint.
    """

    index: int = pydantic.Field()
    """
    The index of the embedding in the list of embeddings.
    """

    embedding: typing.List[float] = pydantic.Field()
    """
    The embedding vector, which is a list of floats. The length of vector depends on the model as listed in the [embedding guide](/docs/guides/embeddings).
    """

    object: EmbeddingObject = pydantic.Field()
    """
    The object type, which is always "embedding".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
