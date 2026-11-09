

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RiskCheckBehaviorFraudRingDetectedLabel(enum.StrEnum):
    """
    Field describing the outcome of a fraud ring behavior risk check.

    `yes` indicates that fraud ring activity was detected.

    `no` indicates that fraud ring activity was not detected.

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
        if self is RiskCheckBehaviorFraudRingDetectedLabel.YES:
            return yes()
        if self is RiskCheckBehaviorFraudRingDetectedLabel.NO:
            return no()
        if self is RiskCheckBehaviorFraudRingDetectedLabel.NO_DATA:
            return no_data()
