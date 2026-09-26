

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TripFaultsItemFault(enum.StrEnum):
    UNSTARTED = "Unstarted"
    DATA_LACKING = "DataLacking"
    UNFINISHED = "Unfinished"

    def visit(
        self,
        unstarted: typing.Callable[[], T_Result],
        data_lacking: typing.Callable[[], T_Result],
        unfinished: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TripFaultsItemFault.UNSTARTED:
            return unstarted()
        if self is TripFaultsItemFault.DATA_LACKING:
            return data_lacking()
        if self is TripFaultsItemFault.UNFINISHED:
            return unfinished()
