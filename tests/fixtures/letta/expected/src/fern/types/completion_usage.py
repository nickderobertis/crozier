

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .completion_tokens_details import CompletionTokensDetails
from .prompt_tokens_details import PromptTokensDetails


class CompletionUsage(UniversalBaseModel):
    """
    Usage statistics for the completion request.
    """

    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    completion_tokens_details: typing.Optional[CompletionTokensDetails] = None
    prompt_tokens_details: typing.Optional[PromptTokensDetails] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
