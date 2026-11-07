

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PackReproducibility(enum.StrEnum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    F = "F"

    def visit(
        self,
        a: typing.Callable[[], T_Result],
        b: typing.Callable[[], T_Result],
        c: typing.Callable[[], T_Result],
        d: typing.Callable[[], T_Result],
        f: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PackReproducibility.A:
            return a()
        if self is PackReproducibility.B:
            return b()
        if self is PackReproducibility.C:
            return c()
        if self is PackReproducibility.D:
            return d()
        if self is PackReproducibility.F:
            return f()
