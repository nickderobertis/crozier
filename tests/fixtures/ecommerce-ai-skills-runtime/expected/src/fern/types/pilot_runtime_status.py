

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pilot_runtime_status_status import PilotRuntimeStatusStatus
from .pilot_runtime_status_stop_reason import PilotRuntimeStatusStopReason
from .pilot_worker_status import PilotWorkerStatus


class PilotRuntimeStatus(UniversalBaseModel):
    status: PilotRuntimeStatusStatus
    boot_id: typing.Optional[str] = None
    generation: typing.Optional[int] = None
    started_at: typing.Optional[dt.datetime] = None
    last_heartbeat_at: typing.Optional[dt.datetime] = None
    stopped_at: typing.Optional[dt.datetime] = None
    stop_reason: typing.Optional[PilotRuntimeStatusStopReason] = None
    workers: typing.List[PilotWorkerStatus]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
