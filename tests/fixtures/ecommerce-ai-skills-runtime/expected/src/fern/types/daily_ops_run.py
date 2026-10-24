

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .daily_ops_brief import DailyOpsBrief
from .daily_ops_run_status import DailyOpsRunStatus
from .daily_ops_schedule_snapshot import DailyOpsScheduleSnapshot
from .daily_ops_source_gap import DailyOpsSourceGap


class DailyOpsRun(UniversalBaseModel):
    id: str
    tenant_id: str
    schedule_id: str
    local_date: dt.date
    timezone: str
    scheduled_for: dt.datetime
    status: DailyOpsRunStatus
    selected_evidence_import_ids: typing.List[str]
    agent_run_id: typing.Optional[str] = None
    graph_version_id: str
    graph_version_hash: str
    schedule_config: DailyOpsScheduleSnapshot
    schedule_config_hash: str
    selected_metric_observation_ids: typing.List[str]
    source_gaps: typing.List[DailyOpsSourceGap]
    brief: typing.Optional[DailyOpsBrief] = None
    error_code: typing.Optional[str] = None
    error_message: typing.Optional[str] = None
    attempt_count: int
    max_attempts: int
    lease_until: typing.Optional[dt.datetime] = None
    completed_at: typing.Optional[dt.datetime] = None
    created_at: dt.datetime
    updated_at: dt.datetime

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
