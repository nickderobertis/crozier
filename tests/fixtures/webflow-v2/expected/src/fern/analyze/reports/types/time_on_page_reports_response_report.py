

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TimeOnPageReportsResponseReport(enum.StrEnum):
    """
    Discriminator identifying the report type.
    """

    TIME_ON_PAGE = "time_on_page"

    def visit(self, time_on_page: typing.Callable[[], T_Result]) -> T_Result:
        if self is TimeOnPageReportsResponseReport.TIME_ON_PAGE:
            return time_on_page()
