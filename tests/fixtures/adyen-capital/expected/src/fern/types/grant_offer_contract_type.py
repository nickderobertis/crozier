

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GrantOfferContractType(enum.StrEnum):
    """
    The contract type of the offer.

    Possible values:
    * **loan**
    * **cashAdvance**
    """

    CASH_ADVANCE = "cashAdvance"
    LOAN = "loan"

    def visit(self, cash_advance: typing.Callable[[], T_Result], loan: typing.Callable[[], T_Result]) -> T_Result:
        if self is GrantOfferContractType.CASH_ADVANCE:
            return cash_advance()
        if self is GrantOfferContractType.LOAN:
            return loan()
