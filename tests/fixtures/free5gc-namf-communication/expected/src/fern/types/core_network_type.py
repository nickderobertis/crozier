

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CoreNetworkType(enum.StrEnum):
    FIVE_GC = "5GC"
    EPC = "EPC"

    def visit(self, five_gc: typing.Callable[[], T_Result], epc: typing.Callable[[], T_Result]) -> T_Result:
        if self is CoreNetworkType.FIVE_GC:
            return five_gc()
        if self is CoreNetworkType.EPC:
            return epc()
