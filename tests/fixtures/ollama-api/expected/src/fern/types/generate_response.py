

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .logprob import Logprob


class GenerateResponse(UniversalBaseModel):
    model: typing.Optional[str] = pydantic.Field(default=None)
    """
    Model name
    """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    ISO 8601 timestamp of response creation
    """

    response: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model's generated text response
    """

    thinking: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model's generated thinking output
    """

    done: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether generation has finished
    """

    done_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason the generation stopped
    """

    total_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time spent generating the response in nanoseconds
    """

    load_duration: typing.Optional[int] = pydantic.Field(default=None)
    """
    Time spent loading the model in nanoseconds
    """

    prompt_eval_count: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of input tokens in the prompt
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
    Number of output tokens generated in the response
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
