

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateEmbeddingResponseUsage(UniversalBaseModel):
    """
    The usage information for the request.
    """

    prompt_tokens: int = pydantic.Field()
    """
    The number of tokens used by the prompt.
    """

    total_tokens: int = pydantic.Field()
    """
    The total number of tokens used by the request.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
