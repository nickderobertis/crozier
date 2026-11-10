

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IncomeVerificationPrecheckConfidence(enum.StrEnum):
    """
    The confidence that Plaid can support the user in the digital income verification flow instead of requiring a manual paystub upload. One of the following:

    `"HIGH"`: It is very likely that this user can use the digital income verification flow.

    "`LOW`": It is unlikely that this user can use the digital income verification flow.

    `"UNKNOWN"`: It was not possible to determine if the user is supportable with the information passed.
    """

    HIGH = "HIGH"
    LOW = "LOW"
    UNKNOWN = "UNKNOWN"

    def visit(
        self,
        high: typing.Callable[[], T_Result],
        low: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IncomeVerificationPrecheckConfidence.HIGH:
            return high()
        if self is IncomeVerificationPrecheckConfidence.LOW:
            return low()
        if self is IncomeVerificationPrecheckConfidence.UNKNOWN:
            return unknown()
