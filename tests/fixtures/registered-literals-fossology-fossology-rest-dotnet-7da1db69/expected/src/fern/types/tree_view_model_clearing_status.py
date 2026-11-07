

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TreeViewModelClearingStatus(enum.StrEnum):
    """
    The clearing status.
    """

    GREEN = "green"
    RED = "red"
    GREY = "grey"
    YELLOW = "yellow"
    RED_GREEN = "redGreen"

    def visit(
        self,
        green: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
        grey: typing.Callable[[], T_Result],
        yellow: typing.Callable[[], T_Result],
        red_green: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TreeViewModelClearingStatus.GREEN:
            return green()
        if self is TreeViewModelClearingStatus.RED:
            return red()
        if self is TreeViewModelClearingStatus.GREY:
            return grey()
        if self is TreeViewModelClearingStatus.YELLOW:
            return yellow()
        if self is TreeViewModelClearingStatus.RED_GREEN:
            return red_green()
