

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransferAuthorizationGuaranteeDecision(enum.StrEnum):
    """
    Indicates whether the transfer is guaranteed by Plaid (Guarantee customers only). This field will contain either `GUARANTEED` or `NOT_GUARANTEED` indicating whether Plaid will guarantee the transfer. If the transfer is not guaranteed, additional information will be provided in the `guarantee_decision_rationale` field. Refer to the `code` field in `guarantee_decision_rationale` for details.
    """

    GUARANTEED = "GUARANTEED"
    NOT_GUARANTEED = "NOT_GUARANTEED"

    def visit(
        self, guaranteed: typing.Callable[[], T_Result], not_guaranteed: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TransferAuthorizationGuaranteeDecision.GUARANTEED:
            return guaranteed()
        if self is TransferAuthorizationGuaranteeDecision.NOT_GUARANTEED:
            return not_guaranteed()
