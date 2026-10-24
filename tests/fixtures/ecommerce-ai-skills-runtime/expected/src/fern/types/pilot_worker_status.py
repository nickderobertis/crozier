

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pilot_worker_status_name import PilotWorkerStatusName
from .pilot_worker_status_status import PilotWorkerStatusStatus


class PilotWorkerStatus(UniversalBaseModel):
    name: PilotWorkerStatusName
    status: PilotWorkerStatusStatus
    iteration_count: int
    consecutive_failures: int
    last_heartbeat_at: dt.datetime
    last_success_at: typing.Optional[dt.datetime] = None
    last_error_at: typing.Optional[dt.datetime] = None
    last_error_type: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
