

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskCheckBehaviorBotDetectedLabel(enum.StrEnum):
    """
    Field describing the outcome of a bot detection behavior risk check.

    `yes` indicates that automated activity was detected.

    `no` indicates that automated activity was not detected.

    `no_data` indicates there was not enough information available to give an accurate signal.
    """

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    def visit(
        self,
        yes: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        no_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RiskCheckBehaviorBotDetectedLabel.YES:
            return yes()
        if self is RiskCheckBehaviorBotDetectedLabel.NO:
            return no()
        if self is RiskCheckBehaviorBotDetectedLabel.NO_DATA:
            return no_data()
