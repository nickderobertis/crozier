

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_tokens_compaction_trigger import InputTokensCompactionTrigger


class CompactionConfig(UniversalBaseModel):
    """
    Uses 80% of the model context length when the explicit trigger is omitted, or 50000 tokens if unknown.
    """

    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Summarize older history when context grows too large. Default: true.
    """

    trigger: typing.Optional[InputTokensCompactionTrigger] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
