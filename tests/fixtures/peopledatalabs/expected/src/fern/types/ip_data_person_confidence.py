

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpDataPersonConfidence(enum.StrEnum):
    """
    How confident we are that the returned person is associated with requested IP.
    """

    VERY_HIGH = "very high"
    HIGH = "high"
    MODERATE = "moderate"
    LOW = "low"
    VERY_LOW = "very low"

    def visit(
        self,
        very_high: typing.Callable[[], T_Result],
        high: typing.Callable[[], T_Result],
        moderate: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        very_low: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpDataPersonConfidence.VERY_HIGH:
            return very_high()
        if self is IpDataPersonConfidence.HIGH:
            return high()
        if self is IpDataPersonConfidence.MODERATE:
            return moderate()
        if self is IpDataPersonConfidence.LOW:
            return low()
        if self is IpDataPersonConfidence.VERY_LOW:
            return very_low()
