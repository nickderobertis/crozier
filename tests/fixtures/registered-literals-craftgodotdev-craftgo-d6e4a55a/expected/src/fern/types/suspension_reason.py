

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SuspensionReason(enum.StrEnum):
    POLICY_VIOLATION = "PolicyViolation"
    PAYMENT_FAILURE = "PaymentFailure"
    OPERATOR_ACTION = "OperatorAction"

    def visit(
        self,
        policy_violation: typing.Callable[[], T_Result],
        payment_failure: typing.Callable[[], T_Result],
        operator_action: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SuspensionReason.POLICY_VIOLATION:
            return policy_violation()
        if self is SuspensionReason.PAYMENT_FAILURE:
            return payment_failure()
        if self is SuspensionReason.OPERATOR_ACTION:
            return operator_action()
