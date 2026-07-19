

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_compatibility_type import ModelCompatibilityType
from .model_effort import ModelEffort
from .model_model_endpoint_type import ModelModelEndpointType
from .model_model_type import ModelModelType
from .model_reasoning_effort import ModelReasoningEffort
from .model_response_format import ModelResponseFormat
from .model_verbosity import ModelVerbosity
from .provider_category import ProviderCategory
from .provider_type import ProviderType


class Model(UniversalBaseModel):
    handle: typing.Optional[str] = pydantic.Field(default=None)
    """
    The handle for this config, in the format provider/model-name.
    """

    name: str = pydantic.Field()
    """
    The actual model name used by the provider
    """

    display_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    A human-friendly display name for the model.
    """

    provider_type: ProviderType = pydantic.Field()
    """
    The type of the provider
    """

    provider_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The provider name for the model.
    """

    model_type: typing.Optional[ModelModelType] = pydantic.Field(default=None)
    """
    Type of model (llm or embedding)
    """

    model: str = pydantic.Field()
    """
    Deprecated: Use 'name' field instead. LLM model name.
    """

    model_endpoint_type: ModelModelEndpointType = pydantic.Field()
    """
    Deprecated: Use 'provider_type' field instead. The endpoint type for the model.
    """

    model_endpoint: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: The endpoint for the model.
    """

    provider_category: typing.Optional[ProviderCategory] = pydantic.Field(default=None)
    """
    Deprecated: The provider category for the model.
    """

    model_wrapper: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: The wrapper for the model.
    """

    context_window: int = pydantic.Field()
    """
    Deprecated: Use 'max_context_window' field instead. The context window size for the model.
    """

    put_inner_thoughts_in_kwargs: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: Puts 'inner_thoughts' as a kwarg in the function call.
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    Deprecated: The temperature to use when generating text with the model.
    """

    max_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated: The maximum number of tokens to generate.
    """

    enable_reasoner: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: Whether or not the model should use extended thinking if it is a 'reasoning' style model.
    """

    reasoning_effort: typing.Optional[ModelReasoningEffort] = pydantic.Field(default=None)
    """
    Deprecated: The reasoning effort to use when generating text reasoning models.
    """

    max_reasoning_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Deprecated: Configurable thinking budget for extended thinking.
    """

    effort: typing.Optional[ModelEffort] = pydantic.Field(default=None)
    """
    The effort level for Anthropic Opus 4.5 model (controls token spending). Not setting this gives similar performance to 'high'.
    """

    frequency_penalty: typing.Optional[float] = pydantic.Field(default=None)
    """
    Deprecated: Positive values penalize new tokens based on their existing frequency in the text so far.
    """

    compatibility_type: typing.Optional[ModelCompatibilityType] = pydantic.Field(default=None)
    """
    Deprecated: The framework compatibility type for the model.
    """

    verbosity: typing.Optional[ModelVerbosity] = pydantic.Field(default=None)
    """
    Deprecated: Soft control for how verbose model output should be.
    """

    tier: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated: The cost tier for the model (cloud only).
    """

    parallel_tool_calls: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Deprecated: If set to True, enables parallel tool calling.
    """

    response_format: typing.Optional[ModelResponseFormat] = pydantic.Field(default=None)
    """
    The response format for the model's output. Supports text, json_object, and json_schema (structured outputs). Can be set via model_settings.
    """

    strict: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable strict mode for tool calling. When true, tool schemas include strict: true and additionalProperties: false, guaranteeing tool outputs match JSON schemas.
    """

    max_context_window: int = pydantic.Field()
    """
    The maximum context window for the model
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
