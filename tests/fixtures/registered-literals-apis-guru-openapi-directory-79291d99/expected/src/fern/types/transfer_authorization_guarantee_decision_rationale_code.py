

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferAuthorizationGuaranteeDecisionRationaleCode(enum.StrEnum):
    """
    A code representing the reason Plaid declined to guarantee this transfer:

    `RETURN_BANK`: The risk of a bank-initiated return (for example, an R01/NSF) is too high to guarantee this transfer.

    `RETURN_CUSTOMER`: The risk of a customer-initiated return (for example, a R10/Unauthorized) is too high to guarantee this transfer.

    `GUARANTEE_LIMIT_REACHED`: This transfer is low-risk, but Guarantee has exhausted an internal limit on the number or rate of guarantees that applies to this transfer.

    `RISK_ESTIMATE_UNAVAILABLE`: A risk estimate is unavailable for this Item.

    `REQUIRED_PARAM_MISSING`: Required fields are missing.
    """

    RETURN_BANK = "RETURN_BANK"
    RETURN_CUSTOMER = "RETURN_CUSTOMER"
    GUARANTEE_LIMIT_REACHED = "GUARANTEE_LIMIT_REACHED"
    RISK_ESTIMATE_UNAVAILABLE = "RISK_ESTIMATE_UNAVAILABLE"
    REQUIRED_PARAM_MISSING = "REQUIRED_PARAM_MISSING"

    def visit(
        self,
        return_bank: typing.Callable[[], T_Result],
        return_customer: typing.Callable[[], T_Result],
        guarantee_limit_reached: typing.Callable[[], T_Result],
        risk_estimate_unavailable: typing.Callable[[], T_Result],
        required_param_missing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransferAuthorizationGuaranteeDecisionRationaleCode.RETURN_BANK:
            return return_bank()
        if self is TransferAuthorizationGuaranteeDecisionRationaleCode.RETURN_CUSTOMER:
            return return_customer()
        if self is TransferAuthorizationGuaranteeDecisionRationaleCode.GUARANTEE_LIMIT_REACHED:
            return guarantee_limit_reached()
        if self is TransferAuthorizationGuaranteeDecisionRationaleCode.RISK_ESTIMATE_UNAVAILABLE:
            return risk_estimate_unavailable()
        if self is TransferAuthorizationGuaranteeDecisionRationaleCode.REQUIRED_PARAM_MISSING:
            return required_param_missing()
