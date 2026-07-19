

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .embedding_model_embedding_endpoint_type import EmbeddingModelEmbeddingEndpointType
from .embedding_model_model_type import EmbeddingModelModelType
from .provider_type import ProviderType


class EmbeddingModel(UniversalBaseModel):
    handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    The handle for this config, in the format provider/model-name.
    """

    name: str = pydantic.Field()
    """
    The actual model name used by the provider
    """

    display_name: str = pydantic.Field()
    """
    Display name for the model shown in UI
    """

    provider_type: ProviderType = pydantic.Field()
    """
    The type of the provider
    """

    provider_name: str = pydantic.Field()
    """
    The name of the provider
    """

    model_type: typing.Optional[EmbeddingModelModelType] = pydantic.Field(default=None)
    """
    Type of model (llm or embedding)
    """

    embedding_endpoint_type: EmbeddingModelEmbeddingEndpointType = pydantic.Field()
    """
    Deprecated: Use 'provider_type' field instead. The endpoint type for the embedding model.
    """

    embedding_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: The endpoint for the model.
    """

    embedding_model: str = pydantic.Field()
    """
    Deprecated: Use 'name' field instead. Embedding model name.
    """

    embedding_dim: int = pydantic.Field()
    """
    The dimension of the embedding
    """

    embedding_chunk_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated: The chunk size of the embedding.
    """

    batch_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated: The maximum batch size for processing embeddings.
    """

    azure_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: The Azure endpoint for the model.
    """

    azure_version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: The Azure version for the model.
    """

    azure_deployment: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: The Azure deployment for the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
