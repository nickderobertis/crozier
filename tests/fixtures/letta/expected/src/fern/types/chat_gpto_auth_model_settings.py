

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_gpto_auth_reasoning import ChatGptoAuthReasoning


class ChatGptoAuthModelSettings(UniversalBaseModel):
    """
    ChatGPT OAuth model configuration (uses ChatGPT backend API).
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

    reasoning: typing.Optional[ChatGptoAuthReasoning] = pydantic.Field(default=None)
    """
    The reasoning configuration for the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
