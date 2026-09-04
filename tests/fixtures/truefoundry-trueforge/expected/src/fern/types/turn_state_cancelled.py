

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .turn_state_cancelled_metrics import TurnStateCancelledMetrics
from .turn_state_cancelled_reason import TurnStateCancelledReason


class TurnStateCancelled(UniversalBaseModel):
    completed_at: str = pydantic.Field()
    """
    ISO 8601 time when cancellation completed.
    """

    metrics: typing.Optional[TurnStateCancelledMetrics] = pydantic.Field(default=None)
    """
    Optional billable aggregate for work done before cancel.
    """

    reason: TurnStateCancelledReason

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
