

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AlertKind(enum.StrEnum):
    ALL = "*"
    BEACON_LIT = "beacon_lit"
    BEACON_OUT = "beacon_out"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        beacon_lit: typing.Callable[[], T_Result],
        beacon_out: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AlertKind.ALL:
            return all_()
        if self is AlertKind.BEACON_LIT:
            return beacon_lit()
        if self is AlertKind.BEACON_OUT:
            return beacon_out()
