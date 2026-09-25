

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TripStateEnum(enum.StrEnum):
    NOMINAL = "Nominal"
    UNSTARTED = "Unstarted"
    DATA_LACKING = "DataLacking"
    UNFINISHED = "Unfinished"

    def visit(
        self,
        nominal: typing.Callable[[], T_Result],
        unstarted: typing.Callable[[], T_Result],
        data_lacking: typing.Callable[[], T_Result],
        unfinished: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TripStateEnum.NOMINAL:
            return nominal()
        if self is TripStateEnum.UNSTARTED:
            return unstarted()
        if self is TripStateEnum.DATA_LACKING:
            return data_lacking()
        if self is TripStateEnum.UNFINISHED:
            return unfinished()
