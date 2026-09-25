

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .turn_state_error_metrics import TurnStateErrorMetrics


class TurnStateError(UniversalBaseModel):
    completed_at: str = pydantic.Field()
    """
    ISO 8601 time when the error state was recorded.
    """

    message: str = pydantic.Field()
    """
    Human-readable error message.
    """

    metrics: typing.Optional[TurnStateErrorMetrics] = pydantic.Field(default=None)
    """
    Optional billable aggregate for work done before the error.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
