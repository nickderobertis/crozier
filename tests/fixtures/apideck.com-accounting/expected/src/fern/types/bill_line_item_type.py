

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class BillLineItemType(str, enum.Enum):
    """
    Bill Line Item type
    """

    EXPENSE_ITEM = "expense_item"
    EXPENSE_ACCOUNT = "expense_account"

    def visit(
        self, expense_item: typing.Callable[[], T_Result], expense_account: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is BillLineItemType.EXPENSE_ITEM:
            return expense_item()
        if self is BillLineItemType.EXPENSE_ACCOUNT:
            return expense_account()
