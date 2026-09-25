

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardCapabilitiesRemoteHornScopeName(enum.StrEnum):
    REMOTE_HORN_WRITE = "remote:horn:write"

    def visit(self, remote_horn_write: typing.Callable[[], T_Result]) -> T_Result:
        if self is OnboardCapabilitiesRemoteHornScopeName.REMOTE_HORN_WRITE:
            return remote_horn_write()
