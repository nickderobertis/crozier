

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class BookMooringRequestTide(enum.StrEnum):
    SLACK = "slack"
    FLOOD = "flood"
    EBB = "ebb"
    NEAP = "neap"

    def visit(
        self,
        slack: typing.Callable[[], T_Result],
        flood: typing.Callable[[], T_Result],
        ebb: typing.Callable[[], T_Result],
        neap: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is BookMooringRequestTide.SLACK:
            return slack()
        if self is BookMooringRequestTide.FLOOD:
            return flood()
        if self is BookMooringRequestTide.EBB:
            return ebb()
        if self is BookMooringRequestTide.NEAP:
            return neap()
