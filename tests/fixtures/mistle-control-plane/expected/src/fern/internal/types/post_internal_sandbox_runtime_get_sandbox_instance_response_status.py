

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus(enum.StrEnum):
    PENDING = "pending"
    STARTING = "starting"
    STARTED = "started"
    INITIALIZING = "initializing"
    RUNNING = "running"
    DEGRADED = "degraded"
    RECONNECTING = "reconnecting"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"

    def visit(
        self,
        pending: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        started: typing.Callable[[], T_Result],
        initializing: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        degraded: typing.Callable[[], T_Result],
        reconnecting: typing.Callable[[], T_Result],
        stopping: typing.Callable[[], T_Result],
        stopped: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.PENDING:
            return pending()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.STARTING:
            return starting()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.STARTED:
            return started()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.INITIALIZING:
            return initializing()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.RUNNING:
            return running()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.DEGRADED:
            return degraded()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.RECONNECTING:
            return reconnecting()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.STOPPING:
            return stopping()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.STOPPED:
            return stopped()
        if self is PostInternalSandboxRuntimeGetSandboxInstanceResponseStatus.FAILED:
            return failed()
