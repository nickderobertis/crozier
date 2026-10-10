

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionMetrics(UniversalBaseModel):
    """
    Rolled-up cost, duration, and turn counters for a session.
    """

    total_cost_in_usd: float
    total_duration_ms: int
    total_turns: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
