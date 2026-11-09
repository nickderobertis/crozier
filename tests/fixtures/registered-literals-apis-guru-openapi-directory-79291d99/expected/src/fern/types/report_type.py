

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportType(enum.StrEnum):
    """
    The report type. It can be `assets` or `income`.
    """

    ASSETS = "assets"
    INCOME = "income"

    def visit(self, assets: typing.Callable[[], T_Result], income: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReportType.ASSETS:
            return assets()
        if self is ReportType.INCOME:
            return income()
