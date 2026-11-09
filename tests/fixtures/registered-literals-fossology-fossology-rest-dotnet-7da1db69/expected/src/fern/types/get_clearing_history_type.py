

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GetClearingHistoryType(enum.StrEnum):
    """
    Type of the clearing
    """

    TO_BE_DISCUSSED = "TO_BE_DISCUSSED"
    IRRELEVANT = "IRRELEVANT"
    IDENTIFIED = "IDENTIFIED"
    DO_NOT_USE = "DO_NOT_USE"
    NON_FUNCTIONAL = "NON_FUNCTIONAL"

    def visit(
        self,
        to_be_discussed: typing.Callable[[], T_Result],
        irrelevant: typing.Callable[[], T_Result],
        identified: typing.Callable[[], T_Result],
        do_not_use: typing.Callable[[], T_Result],
        non_functional: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetClearingHistoryType.TO_BE_DISCUSSED:
            return to_be_discussed()
        if self is GetClearingHistoryType.IRRELEVANT:
            return irrelevant()
        if self is GetClearingHistoryType.IDENTIFIED:
            return identified()
        if self is GetClearingHistoryType.DO_NOT_USE:
            return do_not_use()
        if self is GetClearingHistoryType.NON_FUNCTIONAL:
            return non_functional()
