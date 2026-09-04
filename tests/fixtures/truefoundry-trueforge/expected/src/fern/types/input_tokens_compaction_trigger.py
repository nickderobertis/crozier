

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .input_tokens_compaction_trigger_type import InputTokensCompactionTriggerType


class InputTokensCompactionTrigger(UniversalBaseModel):
    type: InputTokensCompactionTriggerType = pydantic.Field()
    """
    Trigger compaction when the estimated input reaches a token limit.
    """

    value: int = pydantic.Field()
    """
    Estimated input-token count that triggers compaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
