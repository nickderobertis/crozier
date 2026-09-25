

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardCapabilitiesRemoteWakeupScopeName(enum.StrEnum):
    REMOTE_WAKEUP_WRITE = "remote:wakeup:write"

    def visit(self, remote_wakeup_write: typing.Callable[[], T_Result]) -> T_Result:
        if self is OnboardCapabilitiesRemoteWakeupScopeName.REMOTE_WAKEUP_WRITE:
            return remote_wakeup_write()
