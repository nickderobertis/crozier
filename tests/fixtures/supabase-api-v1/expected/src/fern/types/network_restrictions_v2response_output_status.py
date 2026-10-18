

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NetworkRestrictionsV2ResponseOutputStatus(enum.StrEnum):
    STORED = "stored"
    APPLIED = "applied"

    def visit(self, stored: typing.Callable[[], T_Result], applied: typing.Callable[[], T_Result]) -> T_Result:
        if self is NetworkRestrictionsV2ResponseOutputStatus.STORED:
            return stored()
        if self is NetworkRestrictionsV2ResponseOutputStatus.APPLIED:
            return applied()
