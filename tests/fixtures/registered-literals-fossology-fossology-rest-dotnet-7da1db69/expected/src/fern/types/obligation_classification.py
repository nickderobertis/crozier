

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObligationClassification(enum.StrEnum):
    """
    Level of attention this obligation should raise in the clearing process
    """

    GREEN = "green"
    WHITE = "white"
    YELLOW = "yellow"
    RED = "red"

    def visit(
        self,
        green: typing.Callable[[], T_Result],
        white: typing.Callable[[], T_Result],
        yellow: typing.Callable[[], T_Result],
        red: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObligationClassification.GREEN:
            return green()
        if self is ObligationClassification.WHITE:
            return white()
        if self is ObligationClassification.YELLOW:
            return yellow()
        if self is ObligationClassification.RED:
            return red()
