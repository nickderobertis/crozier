

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObReadBalance1DataBalanceItemCreditLineItemType(enum.StrEnum):
    """
    Limit type, in a coded form.
    """

    AVAILABLE = "Available"
    CREDIT = "Credit"
    EMERGENCY = "Emergency"
    PRE_AGREED = "Pre-Agreed"
    TEMPORARY = "Temporary"

    def visit(
        self,
        available: typing.Callable[[], T_Result],
        credit: typing.Callable[[], T_Result],
        emergency: typing.Callable[[], T_Result],
        pre_agreed: typing.Callable[[], T_Result],
        temporary: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObReadBalance1DataBalanceItemCreditLineItemType.AVAILABLE:
            return available()
        if self is ObReadBalance1DataBalanceItemCreditLineItemType.CREDIT:
            return credit()
        if self is ObReadBalance1DataBalanceItemCreditLineItemType.EMERGENCY:
            return emergency()
        if self is ObReadBalance1DataBalanceItemCreditLineItemType.PRE_AGREED:
            return pre_agreed()
        if self is ObReadBalance1DataBalanceItemCreditLineItemType.TEMPORARY:
            return temporary()
