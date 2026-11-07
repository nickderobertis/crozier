

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProviderDeploymentState(enum.StrEnum):
    MISSING = "missing"
    STARTING = "starting"
    READY = "ready"
    RUNNING = "running"
    ERROR = "error"

    def visit(
        self,
        missing: typing.Callable[[], T_Result],
        starting: typing.Callable[[], T_Result],
        ready: typing.Callable[[], T_Result],
        running: typing.Callable[[], T_Result],
        error: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProviderDeploymentState.MISSING:
            return missing()
        if self is ProviderDeploymentState.STARTING:
            return starting()
        if self is ProviderDeploymentState.READY:
            return ready()
        if self is ProviderDeploymentState.RUNNING:
            return running()
        if self is ProviderDeploymentState.ERROR:
            return error()
