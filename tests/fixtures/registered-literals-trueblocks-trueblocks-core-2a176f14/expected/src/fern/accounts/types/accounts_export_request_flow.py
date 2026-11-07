

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AccountsExportRequestFlow(enum.StrEnum):
    IN = "in"
    OUT = "out"
    ZERO = "zero"

    def visit(
        self,
        in_: typing.Callable[[], T_Result],
        out: typing.Callable[[], T_Result],
        zero: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AccountsExportRequestFlow.IN:
            return in_()
        if self is AccountsExportRequestFlow.OUT:
            return out()
        if self is AccountsExportRequestFlow.ZERO:
            return zero()
