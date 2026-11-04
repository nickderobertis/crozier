

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .create_response_body_input import CreateResponseBodyInput
from .create_response_body_reasoning import CreateResponseBodyReasoning
from .create_response_body_service_tier import CreateResponseBodyServiceTier
from .create_response_body_stream_options import CreateResponseBodyStreamOptions
from .create_response_body_text import CreateResponseBodyText
from .create_response_body_tool_choice import CreateResponseBodyToolChoice
from .create_response_body_truncation import CreateResponseBodyTruncation
from .include_enum import IncludeEnum
from .responses_tool_param import ResponsesToolParam


class CreateResponseBody(UniversalBaseModel):
    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model to use for this request, e.g. 'gpt-5.2'.
    """

    input: typing.Optional[CreateResponseBodyInput] = pydantic.Field(default=None)
    """
    Context to provide to the model for the scope of this request. May either be a string or an array of input items. If a string is provided, it is interpreted as a user message.
    """

    previous_response_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the response to use as the prior turn for this request.
    """

    include: typing.Optional[typing.List[IncludeEnum]] = None
    tools: typing.Optional[typing.List[ResponsesToolParam]] = pydantic.Field(default=None)
    """
    A list of tools that the model may call while generating the response.
    """

    tool_choice: typing.Optional[CreateResponseBodyToolChoice] = pydantic.Field(default=None)
    """
    Controls which tool the model should use, if any.
    """

    metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Set of 16 key-value pairs that can be attached to an object. This can be         useful for storing additional information about the object in a structured         format, and querying for objects via API or the dashboard.
            Keys are strings with a maximum length of 64 characters. Values are strings         with a maximum length of 512 characters.
    """

    text: typing.Optional[CreateResponseBodyText] = pydantic.Field(default=None)
    """
    Configuration options for text output.
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    Sampling temperature to use, between 0 and 2. Higher values make the output more random.
    """

    top_p: typing.Optional[float] = pydantic.Field(default=None)
    """
    Nucleus sampling parameter, between 0 and 1. The model considers only the tokens with the top cumulative probability.
    """

    presence_penalty: typing.Optional[float] = pydantic.Field(default=None)
    """
    Penalizes new tokens based on whether they appear in the text so far.
    """

    frequency_penalty: typing.Optional[float] = pydantic.Field(default=None)
    """
    Penalizes new tokens based on their frequency in the text so far.
    """

    parallel_tool_calls: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether the model may call multiple tools in parallel.
    """

    stream: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to stream response events as server-sent events.
    """

    stream_options: typing.Optional[CreateResponseBodyStreamOptions] = pydantic.Field(default=None)
    """
    Options that control streamed response behavior.
    """

    background: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to run the request in the background and return immediately.
    """

    max_output_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of tokens the model may generate for this response.
    """

    max_tool_calls: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum number of tool calls the model may make while generating the response.
    """

    reasoning: typing.Optional[CreateResponseBodyReasoning] = pydantic.Field(default=None)
    """
    Configuration options for reasoning behavior.
    """

    safety_identifier: typing.Optional[str] = pydantic.Field(default=None)
    """
    A stable identifier used for safety monitoring and abuse detection.
    """

    prompt_cache_key: typing.Optional[str] = pydantic.Field(default=None)
    """
    A key to use when reading from or writing to the prompt cache.
    """

    truncation: typing.Optional[CreateResponseBodyTruncation] = pydantic.Field(default=None)
    """
    Controls how the service truncates the input when it exceeds the model context window.
    """

    instructions: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional instructions to guide the model for this request.
    """

    store: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to store the response so it can be retrieved later.
    """

    service_tier: typing.Optional[CreateResponseBodyServiceTier] = pydantic.Field(default=None)
    """
    The service tier to use for this request.
    """

    top_logprobs: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of most likely tokens to return at each position, along with their log probabilities.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
