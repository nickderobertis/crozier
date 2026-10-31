

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .chat_response_message import ChatResponseMessage
from .logprob import Logprob


class ChatResponse(UniversalBaseModel):
    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model name used to generate this message
    """

    created_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Timestamp of response creation (ISO 8601)
    """

    message: typing.Optional[ChatResponseMessage] = None
    done: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the chat response has finished
    """

    done_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason the response finished
    """

    total_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total time spent generating in nanoseconds
    """

    load_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time spent loading the model in nanoseconds
    """

    prompt_eval_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of tokens in the prompt
    """

    prompt_eval_cached_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of prompt tokens read from the cache
    """

    prompt_eval_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time spent evaluating uncached prompt tokens in nanoseconds
    """

    eval_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of tokens generated in the response
    """

    eval_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time spent generating tokens in nanoseconds
    """

    logprobs: typing.Optional[typing.List[Logprob]] = pydantic.Field(default=None)
    """
    Log probability information for the generated tokens when logprobs are enabled
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
