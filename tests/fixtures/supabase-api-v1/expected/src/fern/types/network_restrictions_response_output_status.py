

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NetworkRestrictionsResponseOutputStatus(enum.StrEnum):
    STORED = "stored"
    APPLIED = "applied"

    def visit(self, stored: typing.Callable[[], T_Result], applied: typing.Callable[[], T_Result]) -> T_Result:
        if self is NetworkRestrictionsResponseOutputStatus.STORED:
            return stored()
        if self is NetworkRestrictionsResponseOutputStatus.APPLIED:
            return applied()
