

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SignalDecisionOutcome(enum.StrEnum):
    """
    The payment decision from the risk assessment.

    `APPROVE`: approve the transaction without requiring further actions from your customers. For example, use this field if you are placing a standard hold for all the approved transactions before making funds available to your customers. You should also use this field if you decide to accelerate the fund availability for your customers.

    `REVIEW`: the transaction requires manual review

    `REJECT`: reject the transaction

    `TAKE_OTHER_RISK_MEASURES`: for example, placing a longer hold on funds than those approved transactions or introducing customer frictions such as step-up verification/authentication

    `NOT_EVALUATED`: if only logging the Signal results without using them

    Possible values:  `APPROVE`, `REVIEW`, `REJECT`, `TAKE_OTHER_RISK_MEASURES`, `NOT_EVALUATED`
    """

    APPROVE = "APPROVE"
    REVIEW = "REVIEW"
    REJECT = "REJECT"
    TAKE_OTHER_RISK_MEASURES = "TAKE_OTHER_RISK_MEASURES"
    NOT_EVALUATED = "NOT_EVALUATED"

    def visit(
        self,
        approve: typing.Callable[[], T_Result],
        review: typing.Callable[[], T_Result],
        reject: typing.Callable[[], T_Result],
        take_other_risk_measures: typing.Callable[[], T_Result],
        not_evaluated: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SignalDecisionOutcome.APPROVE:
            return approve()
        if self is SignalDecisionOutcome.REVIEW:
            return review()
        if self is SignalDecisionOutcome.REJECT:
            return reject()
        if self is SignalDecisionOutcome.TAKE_OTHER_RISK_MEASURES:
            return take_other_risk_measures()
        if self is SignalDecisionOutcome.NOT_EVALUATED:
            return not_evaluated()
