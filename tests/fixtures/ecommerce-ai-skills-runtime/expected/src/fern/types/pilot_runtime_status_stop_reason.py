

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PilotRuntimeStatusStopReason(enum.StrEnum):
    GRACEFUL_SHUTDOWN = "graceful_shutdown"
    STARTUP_FAILURE = "startup_failure"
    WORKER_SHUTDOWN_TIMEOUT = "worker_shutdown_timeout"

    def visit(
        self,
        graceful_shutdown: typing.Callable[[], T_Result],
        startup_failure: typing.Callable[[], T_Result],
        worker_shutdown_timeout: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PilotRuntimeStatusStopReason.GRACEFUL_SHUTDOWN:
            return graceful_shutdown()
        if self is PilotRuntimeStatusStopReason.STARTUP_FAILURE:
            return startup_failure()
        if self is PilotRuntimeStatusStopReason.WORKER_SHUTDOWN_TIMEOUT:
            return worker_shutdown_timeout()
