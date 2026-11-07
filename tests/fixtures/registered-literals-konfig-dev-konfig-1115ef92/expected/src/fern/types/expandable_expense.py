

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .expandable_expense_budget import ExpandableExpenseBudget
from .expandable_expense_category import ExpandableExpenseCategory
from .expandable_expense_department import ExpandableExpenseDepartment
from .expandable_expense_location import ExpandableExpenseLocation
from .expandable_expense_merchant import ExpandableExpenseMerchant
from .expandable_expense_payment import ExpandableExpensePayment
from .expandable_expense_payment_status import ExpandableExpensePaymentStatus
from .expandable_expense_status import ExpandableExpenseStatus
from .expandable_expense_user import ExpandableExpenseUser
from .money import Money
from .receipt import Receipt


class ExpandableExpense(UniversalBaseModel):
    """
    The expense object that has expandable fields, e.g., `location`, `department`, and `receipts`.
    """

    id: str = pydantic.Field()
    """
    Unique ID associated with the expense.
    """

    memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    The memo of the expense.
    """

    location_id: typing.Optional[str] = None
    location: typing.Optional[ExpandableExpenseLocation] = pydantic.Field(default=None)
    """
    The location associated with the expense.
    """

    department_id: typing.Optional[str] = None
    department: typing.Optional[ExpandableExpenseDepartment] = pydantic.Field(default=None)
    """
    The department associated with the expense.
    """

    updated_at: dt.datetime = pydantic.Field()
    """
    The last time the expense was updated.
    """

    category: typing.Optional[ExpandableExpenseCategory] = pydantic.Field(default=None)
    """
    The category of expenses.
    """

    merchant_id: typing.Optional[str] = None
    merchant: typing.Optional[ExpandableExpenseMerchant] = None
    receipts: typing.Optional[typing.List[Receipt]] = pydantic.Field(default=None)
    """
    A list of receipts associated with the expense.
    """

    budget_id: typing.Optional[str] = None
    budget: typing.Optional[ExpandableExpenseBudget] = None
    original_amount: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The original amount of the expense is the amount that the employee submitted or incurred for reimbursements or card spends.
    """

    billing_amount: typing.Optional[Money] = pydantic.Field(default=None)
    """
    The billing amount of the expense is the amount that the entity is charged, on the entity's currency, for reimbursements or card spends.
    """

    purchased_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time the purchase was made.
    """

    status: typing.Optional[ExpandableExpenseStatus] = None
    payment_status: typing.Optional[ExpandableExpensePaymentStatus] = None
    user_id: typing.Optional[str] = None
    user: typing.Optional[ExpandableExpenseUser] = None
    payment: typing.Optional[ExpandableExpensePayment] = pydantic.Field(default=None)
    """
    The payment associated with the expense.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
