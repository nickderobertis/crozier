

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compaction_trigger_type import CompactionTriggerType


class CompactionTrigger(UniversalBaseModel):
    """
    Why compaction was triggered.
    """

    context_tokens: int = pydantic.Field()
    """
    Estimated context tokens when compaction fired (prompt + completion).
    """

    threshold_tokens: int = pydantic.Field()
    """
    Configured compaction threshold in tokens.
    """

    type: CompactionTriggerType = pydantic.Field()
    """
    Triggered because estimated context crossed the compaction threshold.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
