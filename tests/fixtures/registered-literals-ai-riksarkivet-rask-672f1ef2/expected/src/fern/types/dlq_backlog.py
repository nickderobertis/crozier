

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .dlq_event import DlqEvent


class DlqBacklog(UniversalBaseModel):
    """
    The outbox saturation snapshot + the visible at-risk events (#83).

    ``depth`` / ``oldest_age_seconds`` are the RAW system-health signal (the same numbers the
    ``outbox.depth`` gauge alerts on); ``events`` is the governed subset the caller may see (≤ depth when
    per-dataset filtering drops events for datasets outside the caller's reach), capped at ``limit``.
    """

    depth: int
    events: typing.List[DlqEvent]
    limit: int
    oldest_age_seconds: float

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
