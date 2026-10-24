

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .daily_ops_brief_graph import DailyOpsBriefGraph
from .daily_ops_brief_inputs import DailyOpsBriefInputs
from .daily_ops_brief_kind import DailyOpsBriefKind
from .daily_ops_brief_review_status import DailyOpsBriefReviewStatus
from .daily_ops_brief_schedule import DailyOpsBriefSchedule
from .daily_ops_brief_status import DailyOpsBriefStatus
from .daily_ops_source_gap import DailyOpsSourceGap


class DailyOpsBrief(UniversalBaseModel):
    schema_version: int
    kind: DailyOpsBriefKind
    status: DailyOpsBriefStatus
    local_date: dt.date
    timezone: str
    scheduled_for: dt.datetime
    generated_at: dt.datetime
    schedule: DailyOpsBriefSchedule
    graph: DailyOpsBriefGraph
    inputs: typing.Optional[DailyOpsBriefInputs] = None
    source_gaps: typing.List[DailyOpsSourceGap]
    agent_run_id: typing.Optional[str] = None
    review_status: typing.Optional[DailyOpsBriefReviewStatus] = None
    reviewer: typing.Optional[typing.Dict[str, typing.Any]] = None
    report: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
