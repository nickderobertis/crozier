

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompletionUsage(UniversalBaseModel):
    """
    Token usage for the compaction model call.
    """

    cache_read_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Optional cache-read tokens.
    """

    cache_write_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Optional cache-write tokens.
    """

    cost_in_usd: typing.Optional[float] = pydantic.Field(default=None)
    """
    Optional estimated cost in USD.
    """

    input_tokens: int = pydantic.Field()
    """
    Input tokens for this completion.
    """

    output_tokens: int = pydantic.Field()
    """
    Output tokens for this completion.
    """

    reasoning_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Optional reasoning tokens.
    """

    total_tokens: int = pydantic.Field()
    """
    Total tokens (input + output).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
