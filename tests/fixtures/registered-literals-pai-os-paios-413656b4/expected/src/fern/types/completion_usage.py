

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompletionUsage(UniversalBaseModel):
    """
    Usage statistics for the completion request.
    """

    completion_tokens: int = pydantic.Field()
    """
    Number of tokens in the generated completion.
    """

    prompt_tokens: int = pydantic.Field()
    """
    Number of tokens in the prompt.
    """

    total_tokens: int = pydantic.Field()
    """
    Total number of tokens used in the request (prompt + completion).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
