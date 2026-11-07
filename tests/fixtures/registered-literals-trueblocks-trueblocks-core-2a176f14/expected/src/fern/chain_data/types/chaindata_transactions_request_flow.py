

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChaindataTransactionsRequestFlow(enum.StrEnum):
    FROM = "from"
    TO = "to"

    def visit(self, from_: typing.Callable[[], T_Result], to: typing.Callable[[], T_Result]) -> T_Result:
        if self is ChaindataTransactionsRequestFlow.FROM:
            return from_()
        if self is ChaindataTransactionsRequestFlow.TO:
            return to()
