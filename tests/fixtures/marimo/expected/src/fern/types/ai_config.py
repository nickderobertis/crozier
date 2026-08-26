

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ai_config_mode import AiConfigMode
from .ai_model_config import AiModelConfig
from .anthropic_config import AnthropicConfig
from .bedrock_config import BedrockConfig
from .git_hub_config import GitHubConfig
from .google_ai_config import GoogleAiConfig
from .open_ai_config import OpenAiConfig


class AiConfig(UniversalBaseModel):
    """
    Configuration options for AI.

        **Keys.**

        - `enabled`: if `False`, hide AI actions and panels in the marimo UI
        - `rules`: custom rules to include in all AI completion prompts
        - `max_tokens`: the maximum number of tokens to use in AI completions
        - `mode`: the mode to use for AI completions. Can be one of: `"ask"` or `"manual"`
        - `inline_tooltip`: if `True`, enable inline AI tooltip suggestions
        - `models`: the models to use for AI completions
        - `open_ai`: the OpenAI config
        - `anthropic`: the Anthropic config
        - `google`: the Google AI config
        - `bedrock`: the Bedrock config
        - `azure`: the Azure config
        - `ollama`: the Ollama config
        - `github`: the GitHub config
        - `openrouter`: the OpenRouter config
        - `wandb`: the Weights & Biases config
        - `opencode_go`: the OpenCode Go config
        - `custom_providers`: a dict of custom OpenAI-compatible providers
        - `open_ai_compatible`: the OpenAI-compatible config (deprecated, use custom_providers)
    """

    anthropic: typing.Optional[AnthropicConfig] = None
    azure: typing.Optional[OpenAiConfig] = None
    bedrock: typing.Optional[BedrockConfig] = None
    custom_providers: typing.Optional[typing.Dict[str, OpenAiConfig]] = None
    enabled: typing.Optional[bool] = None
    github: typing.Optional[GitHubConfig] = None
    google: typing.Optional[GoogleAiConfig] = None
    inline_tooltip: typing.Optional[bool] = None
    max_tokens: typing.Optional[int] = None
    mode: typing.Optional[AiConfigMode] = None
    models: typing.Optional[AiModelConfig] = None
    ollama: typing.Optional[OpenAiConfig] = None
    open_ai: typing.Optional[OpenAiConfig] = None
    open_ai_compatible: typing.Optional[OpenAiConfig] = None
    opencode_go: typing.Optional[OpenAiConfig] = None
    openrouter: typing.Optional[OpenAiConfig] = None
    rules: typing.Optional[str] = None
    wandb: typing.Optional[OpenAiConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
