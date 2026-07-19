

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deepseek_model_settings_response_format import DeepseekModelSettingsResponseFormat


class DeepseekModelSettings(UniversalBaseModel):
    """
    Deepseek model configuration (OpenAI-compatible).
    """

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

    response_format: typing.Optional[DeepseekModelSettingsResponseFormat] = pydantic.Field(default=None)
    """
    The response format for the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
