

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .anthropic_model_settings_effort import AnthropicModelSettingsEffort
from .anthropic_model_settings_response_format import AnthropicModelSettingsResponseFormat
from .anthropic_model_settings_verbosity import AnthropicModelSettingsVerbosity
from .anthropic_thinking import AnthropicThinking


class AnthropicModelSettings(UniversalBaseModel):
    max_output_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of tokens the model can generate.
    """

    parallel_tool_calls: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to enable parallel tool calling.
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    The temperature of the model.
    """

    thinking: typing.Optional[AnthropicThinking] = pydantic.Field(default=None)
    """
    The thinking configuration for the model.
    """

    response_format: typing.Optional[AnthropicModelSettingsResponseFormat] = pydantic.Field(default=None)
    """
    The response format for the model.
    """

    verbosity: typing.Optional[AnthropicModelSettingsVerbosity] = pydantic.Field(default=None)
    """
    Soft control for how verbose model output should be, used for GPT-5 models.
    """

    effort: typing.Optional[AnthropicModelSettingsEffort] = pydantic.Field(default=None)
    """
    Effort level for Opus 4.5 model (controls token conservation). Not setting this gives similar performance to 'high'.
    """

    strict: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Enable strict mode for tool calling. When true, tool outputs are guaranteed to match JSON schemas.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
