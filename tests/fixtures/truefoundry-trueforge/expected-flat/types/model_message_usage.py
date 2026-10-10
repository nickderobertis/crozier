

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_message_usage_input_tokens_breakdown import ModelMessageUsageInputTokensBreakdown


class ModelMessageUsage(UniversalBaseModel):
    cache_read_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Optional cache-read tokens.
    """

    cache_write_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Optional cache-write tokens.
    """

    input_tokens: int = pydantic.Field()
    """
    Input tokens for this model call.
    """

    input_tokens_breakdown: ModelMessageUsageInputTokensBreakdown
    output_tokens: int = pydantic.Field()
    """
    Output tokens for this model call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
