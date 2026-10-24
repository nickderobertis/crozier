

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MissionEventResourceType(enum.StrEnum):
    AGENT_RUN = "agent_run"
    AGENT_TASK = "agent_task"
    REPORT_SYNC = "report_sync"
    JOB = "job"
    DAILY_OPS_RUN = "daily_ops_run"
    PROPOSAL = "proposal"
    PROPOSAL_EXECUTION = "proposal_execution"

    def visit(
        self,
        agent_run: typing.Callable[[], T_Result],
        agent_task: typing.Callable[[], T_Result],
        report_sync: typing.Callable[[], T_Result],
        job: typing.Callable[[], T_Result],
        daily_ops_run: typing.Callable[[], T_Result],
        proposal: typing.Callable[[], T_Result],
        proposal_execution: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MissionEventResourceType.AGENT_RUN:
            return agent_run()
        if self is MissionEventResourceType.AGENT_TASK:
            return agent_task()
        if self is MissionEventResourceType.REPORT_SYNC:
            return report_sync()
        if self is MissionEventResourceType.JOB:
            return job()
        if self is MissionEventResourceType.DAILY_OPS_RUN:
            return daily_ops_run()
        if self is MissionEventResourceType.PROPOSAL:
            return proposal()
        if self is MissionEventResourceType.PROPOSAL_EXECUTION:
            return proposal_execution()
