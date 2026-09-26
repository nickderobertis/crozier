

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemStopSignal(enum.StrEnum):
    SIGTERM = "sigterm"
    SIGKILL = "sigkill"

    def visit(self, sigterm: typing.Callable[[], T_Result], sigkill: typing.Callable[[], T_Result]) -> T_Result:
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemStopSignal.SIGTERM
        ):
            return sigterm()
        if (
            self
            is PostInternalSandboxRuntimeCompilePlanResponseRuntimePlanRuntimeClientsItemProcessesItemStopSignal.SIGKILL
        ):
            return sigkill()
