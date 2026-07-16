

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class State(str, enum.Enum):
    """
    State abbreviation for employee home address
    """

    ACT = "ACT"
    NSW = "NSW"
    NT = "NT"
    QLD = "QLD"
    SA = "SA"
    TAS = "TAS"
    VIC = "VIC"
    WA = "WA"

    def visit(
        self,
        act: typing.Callable[[], T_Result],
        nsw: typing.Callable[[], T_Result],
        nt: typing.Callable[[], T_Result],
        qld: typing.Callable[[], T_Result],
        sa: typing.Callable[[], T_Result],
        tas: typing.Callable[[], T_Result],
        vic: typing.Callable[[], T_Result],
        wa: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is State.ACT:
            return act()
        if self is State.NSW:
            return nsw()
        if self is State.NT:
            return nt()
        if self is State.QLD:
            return qld()
        if self is State.SA:
            return sa()
        if self is State.TAS:
            return tas()
        if self is State.VIC:
            return vic()
        if self is State.WA:
            return wa()
