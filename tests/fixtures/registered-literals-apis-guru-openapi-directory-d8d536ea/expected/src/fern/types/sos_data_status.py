

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SosDataStatus(enum.StrEnum):
    ACTIVE = "Active"

    def visit(self, active: typing.Callable[[], T_Result]) -> T_Result:
        if self is SosDataStatus.ACTIVE:
            return active()
