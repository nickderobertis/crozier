

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.anthropic_model_settings_effort import AnthropicModelSettingsEffort
from ...types.anthropic_model_settings_response_format import AnthropicModelSettingsResponseFormat
from ...types.anthropic_model_settings_verbosity import AnthropicModelSettingsVerbosity
from ...types.anthropic_thinking import AnthropicThinking
from ...types.azure_model_settings_response_format import AzureModelSettingsResponseFormat
from ...types.bedrock_model_settings_response_format import BedrockModelSettingsResponseFormat
from ...types.chat_gpto_auth_reasoning import ChatGptoAuthReasoning
from ...types.deepseek_model_settings_response_format import DeepseekModelSettingsResponseFormat
from ...types.gemini_thinking_config import GeminiThinkingConfig
from ...types.google_ai_model_settings_response_schema import GoogleAiModelSettingsResponseSchema
from ...types.google_vertex_model_settings_response_schema import GoogleVertexModelSettingsResponseSchema
from ...types.groq_model_settings_response_format import GroqModelSettingsResponseFormat
from ...types.open_ai_model_settings_response_format import OpenAiModelSettingsResponseFormat
from ...types.open_ai_reasoning import OpenAiReasoning
from ...types.together_model_settings_response_format import TogetherModelSettingsResponseFormat
from ...types.xai_model_settings_response_format import XaiModelSettingsResponseFormat
from ...types.zai_model_settings_response_format import ZaiModelSettingsResponseFormat


class UpdateAgentModelSettings_Anthropic(UniversalBaseModel):
    provider_type: typing.Literal["anthropic"] = "anthropic"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    thinking: typing.Optional[AnthropicThinking] = None
    response_format: typing.Optional[AnthropicModelSettingsResponseFormat] = None
    verbosity: typing.Optional[AnthropicModelSettingsVerbosity] = None
    effort: typing.Optional[AnthropicModelSettingsEffort] = None
    strict: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_Azure(UniversalBaseModel):
    provider_type: typing.Literal["azure"] = "azure"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    response_format: typing.Optional[AzureModelSettingsResponseFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_Bedrock(UniversalBaseModel):
    provider_type: typing.Literal["bedrock"] = "bedrock"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    response_format: typing.Optional[BedrockModelSettingsResponseFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_ChatgptOauth(UniversalBaseModel):
    provider_type: typing.Literal["chatgpt_oauth"] = "chatgpt_oauth"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    reasoning: typing.Optional[ChatGptoAuthReasoning] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_Deepseek(UniversalBaseModel):
    provider_type: typing.Literal["deepseek"] = "deepseek"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    response_format: typing.Optional[DeepseekModelSettingsResponseFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_GoogleAi(UniversalBaseModel):
    provider_type: typing.Literal["google_ai"] = "google_ai"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    thinking_config: typing.Optional[GeminiThinkingConfig] = None
    response_schema: typing.Optional[GoogleAiModelSettingsResponseSchema] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_GoogleVertex(UniversalBaseModel):
    provider_type: typing.Literal["google_vertex"] = "google_vertex"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    thinking_config: typing.Optional[GeminiThinkingConfig] = None
    response_schema: typing.Optional[GoogleVertexModelSettingsResponseSchema] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_Groq(UniversalBaseModel):
    provider_type: typing.Literal["groq"] = "groq"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    response_format: typing.Optional[GroqModelSettingsResponseFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_Openai(UniversalBaseModel):
    provider_type: typing.Literal["openai"] = "openai"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    reasoning: typing.Optional[OpenAiReasoning] = None
    response_format: typing.Optional[OpenAiModelSettingsResponseFormat] = None
    strict: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_Together(UniversalBaseModel):
    provider_type: typing.Literal["together"] = "together"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    response_format: typing.Optional[TogetherModelSettingsResponseFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_Xai(UniversalBaseModel):
    provider_type: typing.Literal["xai"] = "xai"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    response_format: typing.Optional[XaiModelSettingsResponseFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class UpdateAgentModelSettings_Zai(UniversalBaseModel):
    provider_type: typing.Literal["zai"] = "zai"
    max_output_tokens: typing.Optional[int] = None
    parallel_tool_calls: typing.Optional[bool] = None
    temperature: typing.Optional[float] = None
    response_format: typing.Optional[ZaiModelSettingsResponseFormat] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


UpdateAgentModelSettings = typing_extensions.Annotated[
    typing.Union[
        UpdateAgentModelSettings_Anthropic,
        UpdateAgentModelSettings_Azure,
        UpdateAgentModelSettings_Bedrock,
        UpdateAgentModelSettings_ChatgptOauth,
        UpdateAgentModelSettings_Deepseek,
        UpdateAgentModelSettings_GoogleAi,
        UpdateAgentModelSettings_GoogleVertex,
        UpdateAgentModelSettings_Groq,
        UpdateAgentModelSettings_Openai,
        UpdateAgentModelSettings_Together,
        UpdateAgentModelSettings_Xai,
        UpdateAgentModelSettings_Zai,
    ],
    pydantic.Field(discriminator="provider_type"),
]
