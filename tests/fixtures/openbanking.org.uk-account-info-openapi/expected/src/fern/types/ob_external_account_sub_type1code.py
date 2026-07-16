

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ObExternalAccountSubType1Code(str, enum.Enum):
    """
    Specifies the sub type of account (product family group).
    """

    CHARGE_CARD = "ChargeCard"
    CREDIT_CARD = "CreditCard"
    CURRENT_ACCOUNT = "CurrentAccount"
    E_MONEY = "EMoney"
    LOAN = "Loan"
    MORTGAGE = "Mortgage"
    PRE_PAID_CARD = "PrePaidCard"
    SAVINGS = "Savings"

    def visit(
        self,
        charge_card: typing.Callable[[], T_Result],
        credit_card: typing.Callable[[], T_Result],
        current_account: typing.Callable[[], T_Result],
        e_money: typing.Callable[[], T_Result],
        loan: typing.Callable[[], T_Result],
        mortgage: typing.Callable[[], T_Result],
        pre_paid_card: typing.Callable[[], T_Result],
        savings: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObExternalAccountSubType1Code.CHARGE_CARD:
            return charge_card()
        if self is ObExternalAccountSubType1Code.CREDIT_CARD:
            return credit_card()
        if self is ObExternalAccountSubType1Code.CURRENT_ACCOUNT:
            return current_account()
        if self is ObExternalAccountSubType1Code.E_MONEY:
            return e_money()
        if self is ObExternalAccountSubType1Code.LOAN:
            return loan()
        if self is ObExternalAccountSubType1Code.MORTGAGE:
            return mortgage()
        if self is ObExternalAccountSubType1Code.PRE_PAID_CARD:
            return pre_paid_card()
        if self is ObExternalAccountSubType1Code.SAVINGS:
            return savings()
