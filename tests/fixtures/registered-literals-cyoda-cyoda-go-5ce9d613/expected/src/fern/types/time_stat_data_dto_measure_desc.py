

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TimeStatDataDtoMeasureDesc(enum.StrEnum):
    """
    Suggested unit abbreviation for displaying timing values based on magnitude analysis
    """

    NS = "ns"
    US = "us"
    MS = "ms"

    def visit(
        self, ns: typing.Callable[[], T_Result], us: typing.Callable[[], T_Result], ms: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TimeStatDataDtoMeasureDesc.NS:
            return ns()
        if self is TimeStatDataDtoMeasureDesc.US:
            return us()
        if self is TimeStatDataDtoMeasureDesc.MS:
            return ms()
