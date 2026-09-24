

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardCapabilitiesRemoteDoorScopeName(enum.StrEnum):
    REMOTE_DOOR_WRITE = "remote:door:write"

    def visit(self, remote_door_write: typing.Callable[[], T_Result]) -> T_Result:
        if self is OnboardCapabilitiesRemoteDoorScopeName.REMOTE_DOOR_WRITE:
            return remote_door_write()
