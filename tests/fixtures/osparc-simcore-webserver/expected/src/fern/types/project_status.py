

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectStatus(enum.StrEnum):
    CLOSED = "CLOSED"
    CLOSING = "CLOSING"
    CLONING = "CLONING"
    EXPORTING = "EXPORTING"
    OPENING = "OPENING"
    OPENED = "OPENED"
    MAINTAINING = "MAINTAINING"

    def visit(
        self,
        closed: typing.Callable[[], T_Result],
        closing: typing.Callable[[], T_Result],
        cloning: typing.Callable[[], T_Result],
        exporting: typing.Callable[[], T_Result],
        opening: typing.Callable[[], T_Result],
        opened: typing.Callable[[], T_Result],
        maintaining: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectStatus.CLOSED:
            return closed()
        if self is ProjectStatus.CLOSING:
            return closing()
        if self is ProjectStatus.CLONING:
            return cloning()
        if self is ProjectStatus.EXPORTING:
            return exporting()
        if self is ProjectStatus.OPENING:
            return opening()
        if self is ProjectStatus.OPENED:
            return opened()
        if self is ProjectStatus.MAINTAINING:
            return maintaining()
