

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReportRequestReason(enum.StrEnum):
    """
    Reason for the report
    """

    MATURE = "mature"
    DMCA = "dmca"
    OTHER = "other"

    def visit(
        self,
        mature: typing.Callable[[], T_Result],
        dmca: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ReportRequestReason.MATURE:
            return mature()
        if self is ReportRequestReason.DMCA:
            return dmca()
        if self is ReportRequestReason.OTHER:
            return other()
