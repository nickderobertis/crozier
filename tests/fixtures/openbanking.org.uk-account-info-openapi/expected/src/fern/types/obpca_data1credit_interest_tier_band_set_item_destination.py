

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObpcaData1CreditInterestTierBandSetItemDestination(str, enum.Enum):
    """
    Describes whether accrued interest is payable only to the PCA or to another bank account
    """

    PAY_AWAY = "PayAway"
    SELF_CREDIT = "SelfCredit"

    def visit(self, pay_away: typing.Callable[[], T_Result], self_credit: typing.Callable[[], T_Result]) -> T_Result:
        if self is ObpcaData1CreditInterestTierBandSetItemDestination.PAY_AWAY:
            return pay_away()
        if self is ObpcaData1CreditInterestTierBandSetItemDestination.SELF_CREDIT:
            return self_credit()
