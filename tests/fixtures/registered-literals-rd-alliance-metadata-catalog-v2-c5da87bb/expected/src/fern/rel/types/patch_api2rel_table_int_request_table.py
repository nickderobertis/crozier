

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchApi2RelTableIntRequestTable(enum.StrEnum):
    M = "m"
    T = "t"
    C = "c"
    E = "e"

    def visit(
        self,
        m: typing.Callable[[], T_Result],
        t: typing.Callable[[], T_Result],
        c: typing.Callable[[], T_Result],
        e: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchApi2RelTableIntRequestTable.M:
            return m()
        if self is PatchApi2RelTableIntRequestTable.T:
            return t()
        if self is PatchApi2RelTableIntRequestTable.C:
            return c()
        if self is PatchApi2RelTableIntRequestTable.E:
            return e()
