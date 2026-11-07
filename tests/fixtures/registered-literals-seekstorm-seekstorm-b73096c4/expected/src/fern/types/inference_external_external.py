

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .precision import Precision
from .quantization import Quantization
from .vector_similarity import VectorSimilarity


class InferenceExternalExternal(UniversalBaseModel):
    """
    External inference
    """

    dimensions: int = pydantic.Field()
    """
    Number of dimensions for the embeddings.
    """

    precision: Precision = pydantic.Field()
    """
    Data type for embeddings.
    """

    quantization: Quantization = pydantic.Field()
    """
    Quantization method for embeddings.
    """

    similarity: VectorSimilarity = pydantic.Field()
    """
    Similarity metric to use for comparing embeddings, e.g. cosine similarity or euclidean distance.
    This should be the same similarity metric that was used during the training of the embedding model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
