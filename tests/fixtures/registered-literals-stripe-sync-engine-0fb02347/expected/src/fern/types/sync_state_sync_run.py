

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .progress_payload import ProgressPayload


class SyncStateSyncRun(UniversalBaseModel):
    """
    Engine-managed run state — run_id, time_ceiling, accumulated progress.
    """

    run_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identifies a finite backfill run. Omit for continuous sync.
    """

    time_ceiling: typing.Optional[str] = pydantic.Field(default=None)
    """
    Frozen upper bound (ISO 8601). Set on first invocation when run_id is present; reused on continuation.
    """

    progress: ProgressPayload = pydantic.Field()
    """
    Accumulated progress from prior requests in this run.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
