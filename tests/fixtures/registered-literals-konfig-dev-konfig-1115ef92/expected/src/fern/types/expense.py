

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .expense_category import ExpenseCategory
from .expense_payment_status import ExpensePaymentStatus
from .expense_status import ExpenseStatus
from .money import Money


class Expense(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique ID associated with the expense.
    """

    memo: typing.Optional[str] = pydantic.Field(default=None)
    """
    The memo of the expense.
    """

    location_id: typing.Optional[str] = None
    department_id: typing.Optional[str] = None
    updated_at: dt.datetime = pydantic.Field()
    """
    The last time the expense was updated.
    """

    category: typing.Optional[ExpenseCategory] = pydantic.Field(default=None)
    """
    The category of expenses.
    """

    merchant_id: typing.Optional[str] = None
    budget_id: typing.Optional[str] = None
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

    status: typing.Optional[ExpenseStatus] = None
    payment_status: typing.Optional[ExpensePaymentStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
