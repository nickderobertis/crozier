

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DepotRecordStatus(enum.StrEnum):
    STORED = "stored"
    RELEASED = "released"

    def visit(self, stored: typing.Callable[[], T_Result], released: typing.Callable[[], T_Result]) -> T_Result:
        if self is DepotRecordStatus.STORED:
            return stored()
        if self is DepotRecordStatus.RELEASED:
            return released()
