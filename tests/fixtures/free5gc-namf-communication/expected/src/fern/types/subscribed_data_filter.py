

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SubscribedDataFilter(enum.StrEnum):
    SARI = "SARI"
    RFSP_INDEX = "RFSP_INDEX"

    def visit(self, sari: typing.Callable[[], T_Result], rfsp_index: typing.Callable[[], T_Result]) -> T_Result:
        if self is SubscribedDataFilter.SARI:
            return sari()
        if self is SubscribedDataFilter.RFSP_INDEX:
            return rfsp_index()
