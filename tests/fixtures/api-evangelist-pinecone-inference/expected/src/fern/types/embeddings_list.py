

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding import Embedding
from .embeddings_list_usage import EmbeddingsListUsage


class EmbeddingsList(UniversalBaseModel):
    """
    Embeddings generated for the input.
    """

    model: str = pydantic.Field()
    """
    The model used to generate the embeddings
    """

    vector_type: str = pydantic.Field()
    """
    Indicates whether the response data contains 'dense' or 'sparse' embeddings.
    """

    data: typing.List[Embedding] = pydantic.Field()
    """
    The embeddings generated for the inputs.
    """

    usage: EmbeddingsListUsage = pydantic.Field()
    """
    Usage statistics for the model inference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
