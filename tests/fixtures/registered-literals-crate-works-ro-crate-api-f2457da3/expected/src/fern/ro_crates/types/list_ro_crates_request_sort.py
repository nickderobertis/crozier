

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListRoCratesRequestSort(enum.StrEnum):
    ID = "id"
    LAST_DEPOSITED_AT = "lastDepositedAt"

    def visit(self, id: typing.Callable[[], T_Result], last_deposited_at: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListRoCratesRequestSort.ID:
            return id()
        if self is ListRoCratesRequestSort.LAST_DEPOSITED_AT:
            return last_deposited_at()
