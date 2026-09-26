

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OnboardCapabilitiesRemoteChargingScopeName(enum.StrEnum):
    REMOTE_CHARGING_WRITE = "remote:charging:write"

    def visit(self, remote_charging_write: typing.Callable[[], T_Result]) -> T_Result:
        if self is OnboardCapabilitiesRemoteChargingScopeName.REMOTE_CHARGING_WRITE:
            return remote_charging_write()
