

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .gemini_thinking_config import GeminiThinkingConfig
from .google_vertex_model_settings_response_schema import GoogleVertexModelSettingsResponseSchema


class GoogleVertexModelSettings(UniversalBaseModel):
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

    thinking_config: typing.Optional[GeminiThinkingConfig] = pydantic.Field(default=None)
    """
    The thinking configuration for the model.
    """

    response_schema: typing.Optional[GoogleVertexModelSettingsResponseSchema] = pydantic.Field(default=None)
    """
    The response schema for the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
