

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class WorkqueuesGetResponseItemState(enum.StrEnum):
    R = "R"
    S = "S"
    D = "D"
    Z = "Z"
    T = "T"
    W = "W"
    X = "X"
    K = "K"
    P = "P"

    def visit(
        self,
        r: typing.Callable[[], T_Result],
        s: typing.Callable[[], T_Result],
        d: typing.Callable[[], T_Result],
        z: typing.Callable[[], T_Result],
        t: typing.Callable[[], T_Result],
        w: typing.Callable[[], T_Result],
        x: typing.Callable[[], T_Result],
        k: typing.Callable[[], T_Result],
        p: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WorkqueuesGetResponseItemState.R:
            return r()
        if self is WorkqueuesGetResponseItemState.S:
            return s()
        if self is WorkqueuesGetResponseItemState.D:
            return d()
        if self is WorkqueuesGetResponseItemState.Z:
            return z()
        if self is WorkqueuesGetResponseItemState.T:
            return t()
        if self is WorkqueuesGetResponseItemState.W:
            return w()
        if self is WorkqueuesGetResponseItemState.X:
            return x()
        if self is WorkqueuesGetResponseItemState.K:
            return k()
        if self is WorkqueuesGetResponseItemState.P:
            return p()
