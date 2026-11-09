

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateMaintenanceOptionsItem(enum.StrEnum):
    A = "a"
    F = "F"
    G = "g"
    E = "E"
    L = "L"
    N = "N"
    R = "R"
    T = "t"
    D = "D"
    Z = "Z"
    I = "I"
    V = "v"
    O = "o"

    def visit(
        self,
        a: typing.Callable[[], T_Result],
        f: typing.Callable[[], T_Result],
        g: typing.Callable[[], T_Result],
        e: typing.Callable[[], T_Result],
        l: typing.Callable[[], T_Result],
        n: typing.Callable[[], T_Result],
        r: typing.Callable[[], T_Result],
        t: typing.Callable[[], T_Result],
        d: typing.Callable[[], T_Result],
        z: typing.Callable[[], T_Result],
        i: typing.Callable[[], T_Result],
        v: typing.Callable[[], T_Result],
        o: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreateMaintenanceOptionsItem.A:
            return a()
        if self is CreateMaintenanceOptionsItem.F:
            return f()
        if self is CreateMaintenanceOptionsItem.G:
            return g()
        if self is CreateMaintenanceOptionsItem.E:
            return e()
        if self is CreateMaintenanceOptionsItem.L:
            return l()
        if self is CreateMaintenanceOptionsItem.N:
            return n()
        if self is CreateMaintenanceOptionsItem.R:
            return r()
        if self is CreateMaintenanceOptionsItem.T:
            return t()
        if self is CreateMaintenanceOptionsItem.D:
            return d()
        if self is CreateMaintenanceOptionsItem.Z:
            return z()
        if self is CreateMaintenanceOptionsItem.I:
            return i()
        if self is CreateMaintenanceOptionsItem.V:
            return v()
        if self is CreateMaintenanceOptionsItem.O:
            return o()
