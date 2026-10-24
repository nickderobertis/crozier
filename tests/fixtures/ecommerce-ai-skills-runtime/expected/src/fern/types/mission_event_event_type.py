

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class MissionEventEventType(enum.StrEnum):
    AGENT_RUN_CREATED = "agent_run.created"
    AGENT_RUN_STATUS_CHANGED = "agent_run.status_changed"
    AGENT_TASK_CREATED = "agent_task.created"
    AGENT_TASK_STATUS_CHANGED = "agent_task.status_changed"
    REPORT_SYNC_CREATED = "report_sync.created"
    REPORT_SYNC_STATUS_CHANGED = "report_sync.status_changed"
    JOB_CREATED = "job.created"
    JOB_STATUS_CHANGED = "job.status_changed"
    DAILY_OPS_RUN_CREATED = "daily_ops_run.created"
    DAILY_OPS_RUN_STATUS_CHANGED = "daily_ops_run.status_changed"
    PROPOSAL_CREATED = "proposal.created"
    PROPOSAL_STATUS_CHANGED = "proposal.status_changed"
    PROPOSAL_EXECUTION_CREATED = "proposal_execution.created"
    PROPOSAL_EXECUTION_STATUS_CHANGED = "proposal_execution.status_changed"

    def visit(
        self,
        agent_run_created: typing.Callable[[], T_Result],
        agent_run_status_changed: typing.Callable[[], T_Result],
        agent_task_created: typing.Callable[[], T_Result],
        agent_task_status_changed: typing.Callable[[], T_Result],
        report_sync_created: typing.Callable[[], T_Result],
        report_sync_status_changed: typing.Callable[[], T_Result],
        job_created: typing.Callable[[], T_Result],
        job_status_changed: typing.Callable[[], T_Result],
        daily_ops_run_created: typing.Callable[[], T_Result],
        daily_ops_run_status_changed: typing.Callable[[], T_Result],
        proposal_created: typing.Callable[[], T_Result],
        proposal_status_changed: typing.Callable[[], T_Result],
        proposal_execution_created: typing.Callable[[], T_Result],
        proposal_execution_status_changed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is MissionEventEventType.AGENT_RUN_CREATED:
            return agent_run_created()
        if self is MissionEventEventType.AGENT_RUN_STATUS_CHANGED:
            return agent_run_status_changed()
        if self is MissionEventEventType.AGENT_TASK_CREATED:
            return agent_task_created()
        if self is MissionEventEventType.AGENT_TASK_STATUS_CHANGED:
            return agent_task_status_changed()
        if self is MissionEventEventType.REPORT_SYNC_CREATED:
            return report_sync_created()
        if self is MissionEventEventType.REPORT_SYNC_STATUS_CHANGED:
            return report_sync_status_changed()
        if self is MissionEventEventType.JOB_CREATED:
            return job_created()
        if self is MissionEventEventType.JOB_STATUS_CHANGED:
            return job_status_changed()
        if self is MissionEventEventType.DAILY_OPS_RUN_CREATED:
            return daily_ops_run_created()
        if self is MissionEventEventType.DAILY_OPS_RUN_STATUS_CHANGED:
            return daily_ops_run_status_changed()
        if self is MissionEventEventType.PROPOSAL_CREATED:
            return proposal_created()
        if self is MissionEventEventType.PROPOSAL_STATUS_CHANGED:
            return proposal_status_changed()
        if self is MissionEventEventType.PROPOSAL_EXECUTION_CREATED:
            return proposal_execution_created()
        if self is MissionEventEventType.PROPOSAL_EXECUTION_STATUS_CHANGED:
            return proposal_execution_status_changed()
