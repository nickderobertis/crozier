

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GenerateStreamEvent(UniversalBaseModel):
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
    The model's generated text response for this chunk
    """

    thinking: typing.Optional[str] = pydantic.Field(default=None)
    """
    The model's generated thinking output for this chunk
    """

    done: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Indicates whether the stream has finished
    """

    done_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason streaming finished
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
