

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunningState(enum.StrEnum):
    """
    State of execution of a project's computational workflow

    SEE StateType for task state

    # Computational backend states explained:
    - UNKNOWN - The backend doesn't know about the task anymore, it has disappeared from the system or it was never created (eg. when we are asking for the task)
    - NOT_STARTED - Default state when the task is created
    - PUBLISHED - The task has been submitted to the computational backend (click on "Run" button in the UI)
    - PENDING - Task has been transferred to the Dask scheduler and is waiting for a worker to pick it up (director-v2 --> Dask scheduler)
       - But! it is also transition state (ex. PENDING -> WAITING_FOR_CLUSTER -> PENDING -> WAITING_FOR_RESOURCES -> PENDING -> STARTED)
    - WAITING_FOR_CLUSTER - No cluster (Dask scheduler) is available to run the task; waiting for one to become available
    - WAITING_FOR_RESOURCES - No worker (Dask worker) is available to run the task; waiting for one to become available
    - STARTED - A worker has picked up the task and is executing it
    - SUCCESS - Task finished successfully
    - FAILED - Task finished with an error
    - ABORTED - Task was aborted before completion
    """

    UNKNOWN = "UNKNOWN"
    NOT_STARTED = "NOT_STARTED"
    PUBLISHED = "PUBLISHED"
    PENDING = "PENDING"
    WAITING_FOR_CLUSTER = "WAITING_FOR_CLUSTER"
    WAITING_FOR_RESOURCES = "WAITING_FOR_RESOURCES"
    STARTED = "STARTED"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    ABORTED = "ABORTED"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        not_started: typing.Callable[[], T_Result],
        published: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
        waiting_for_cluster: typing.Callable[[], T_Result],
        waiting_for_resources: typing.Callable[[], T_Result],
        started: typing.Callable[[], T_Result],
        success: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunningState.UNKNOWN:
            return unknown()
        if self is RunningState.NOT_STARTED:
            return not_started()
        if self is RunningState.PUBLISHED:
            return published()
        if self is RunningState.PENDING:
            return pending()
        if self is RunningState.WAITING_FOR_CLUSTER:
            return waiting_for_cluster()
        if self is RunningState.WAITING_FOR_RESOURCES:
            return waiting_for_resources()
        if self is RunningState.STARTED:
            return started()
        if self is RunningState.SUCCESS:
            return success()
        if self is RunningState.FAILED:
            return failed()
        if self is RunningState.ABORTED:
            return aborted()
