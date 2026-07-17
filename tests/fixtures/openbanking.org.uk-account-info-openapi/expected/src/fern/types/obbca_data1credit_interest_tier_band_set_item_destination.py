

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObbcaData1CreditInterestTierBandSetItemDestination(enum.StrEnum):
    """
    Describes whether accrued interest is payable only to the BCA or to another bank account
    """

    PAY_AWAY = "PayAway"
    SELF_CREDIT = "SelfCredit"

    def visit(self, pay_away: typing.Callable[[], T_Result], self_credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObbcaData1CreditInterestTierBandSetItemDestination.PAY_AWAY:
            return pay_away()
        if self is ObbcaData1CreditInterestTierBandSetItemDestination.SELF_CREDIT:
            return self_credit()
