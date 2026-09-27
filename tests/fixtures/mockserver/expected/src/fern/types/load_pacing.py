

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .load_pacing_mode import LoadPacingMode


class LoadPacing(UniversalBaseModel):
    """
    adaptive iteration pacing (think-time) for a load scenario: a target per-virtual-user iteration cycle time. After a closed-model VU finishes one pass through the steps, the orchestrator waits whatever remains of the target cycle before launching that VU's next iteration; on overrun the next iteration starts immediately (no wait). Applies only to the closed-model VU loop — open-model RATE iterations ignore it, their arrival rate already governing spacing — and composes with per-step thinkTime. In-flight latency measurement is unchanged; pacing only affects when the next iteration launches.
    """

    mode: LoadPacingMode = pydantic.Field()
    """
    how the target iteration cycle is derived from value: NONE = no pacing (immediate reschedule); CONSTANT_PACING = value is the target cycle in milliseconds; CONSTANT_THROUGHPUT = value is the target iterations/second per VU (cycle = 1000 / value ms)
    """

    value: float = pydantic.Field()
    """
    for CONSTANT_PACING the target cycle in milliseconds; for CONSTANT_THROUGHPUT the target iterations/second per VU. Must be > 0 when mode is not NONE; ignored when mode is NONE.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
