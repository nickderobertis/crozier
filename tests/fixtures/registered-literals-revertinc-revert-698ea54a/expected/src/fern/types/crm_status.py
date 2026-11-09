

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CrmStatus(enum.StrEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

    def visit(self, active: typing.Callable[[], T_Result], inactive: typing.Callable[[], T_Result]) -> T_Result:
        if self is CrmStatus.ACTIVE:
            return active()
        if self is CrmStatus.INACTIVE:
            return inactive()
