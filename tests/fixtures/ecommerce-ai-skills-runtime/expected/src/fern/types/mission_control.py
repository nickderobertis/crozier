

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .action import Action
from .agent_run import AgentRun
from .job import Job
from .mission_event_cursor import MissionEventCursor
from .schedule import Schedule


class MissionControl(UniversalBaseModel):
    """
    Snapshot fields may grow additively; clients must ignore unrecognized fields.
    """

    counts: typing.Dict[str, typing.Any]
    event_cursor: MissionEventCursor
    approval_inbox: typing.List[Action]
    failed_runs: typing.List[AgentRun]
    failed_jobs: typing.List[Job]
    recent_runs: typing.List[AgentRun]
    schedules: typing.List[Schedule]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
