

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class TrafficReportsResponseReport(enum.StrEnum):
    """
    Discriminator identifying the report type.
    """

    TRAFFIC = "traffic"

    def visit(self, traffic: typing.Callable[[], T_Result]) -> T_Result:
        if self is TrafficReportsResponseReport.TRAFFIC:
            return traffic()
