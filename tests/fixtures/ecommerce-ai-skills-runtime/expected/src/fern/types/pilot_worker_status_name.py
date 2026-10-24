

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotWorkerStatusName(enum.StrEnum):
    SCHEDULER = "scheduler"
    JOB_WORKER = "job_worker"
    REPORT_WORKER = "report_worker"
    DAILY_SCHEDULER = "daily_scheduler"
    DAILY_WORKER = "daily_worker"
    PROPOSAL_WORKER = "proposal_worker"

    def visit(
        self,
        scheduler: typing.Callable[[], T_Result],
        job_worker: typing.Callable[[], T_Result],
        report_worker: typing.Callable[[], T_Result],
        daily_scheduler: typing.Callable[[], T_Result],
        daily_worker: typing.Callable[[], T_Result],
        proposal_worker: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PilotWorkerStatusName.SCHEDULER:
            return scheduler()
        if self is PilotWorkerStatusName.JOB_WORKER:
            return job_worker()
        if self is PilotWorkerStatusName.REPORT_WORKER:
            return report_worker()
        if self is PilotWorkerStatusName.DAILY_SCHEDULER:
            return daily_scheduler()
        if self is PilotWorkerStatusName.DAILY_WORKER:
            return daily_worker()
        if self is PilotWorkerStatusName.PROPOSAL_WORKER:
            return proposal_worker()
