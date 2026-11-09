

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetFileIprasRequestStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetFileIprasRequestStatus.ACTIVE:
            return active()
        if self is GetFileIprasRequestStatus.INACTIVE:
            return inactive()
