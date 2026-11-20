

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_info_supported_metrics import ModelInfoSupportedMetrics
from .model_info_supported_parameter import ModelInfoSupportedParameter


class ModelInfo(UniversalBaseModel):
    """
    Represents the model configuration including model type, supported parameters, and other model details.
    """

    model: str = pydantic.Field()
    """
    The name of the model.
    """

    short_description: str = pydantic.Field()
    """
    A summary of the model.
    """

    type: str = pydantic.Field()
    """
    The type of model (e.g. 'embed' or 'rerank').
    """

    vector_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Whether the embedding model produces 'dense' or 'sparse' embeddings.
    """

    default_dimension: typing.Optional[int] = pydantic.Field(default=None)
    """
    The default embedding model dimension (applies to dense embedding models only).
    """

    modality: typing.Optional[str] = pydantic.Field(default=None)
    """
    The modality of the model (e.g. 'text').
    """

    max_sequence_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum tokens per sequence supported by the model.
    """

    max_batch_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum batch size (number of sequences) supported by the model.
    """

    provider_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the provider of the model.
    """

    supported_dimensions: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    The list of supported dimensions for the model (applies to dense embedding models only).
    """

    supported_metrics: typing.Optional[ModelInfoSupportedMetrics] = None
    supported_parameters: typing.List[ModelInfoSupportedParameter] = pydantic.Field()
    """
    List of parameters supported by the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
