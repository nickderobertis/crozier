

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .personal_finance_category import PersonalFinanceCategory
from .recurring_transaction_frequency import RecurringTransactionFrequency
from .transaction_stream_amount import TransactionStreamAmount
from .transaction_stream_status import TransactionStreamStatus


class TransactionStream(UniversalBaseModel):
    """
    A grouping of related transactions
    """

    account_id: str = pydantic.Field()
    """
    The ID of the account to which the stream belongs
    """

    average_amount: TransactionStreamAmount
    category: typing.List[str] = pydantic.Field()
    """
    A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).
    """

    category_id: str = pydantic.Field()
    """
    The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget).
    """

    description: str = pydantic.Field()
    """
    A description of the transaction stream.
    """

    first_date: dt.date = pydantic.Field()
    """
    The posted date of the earliest transaction in the stream.
    """

    frequency: RecurringTransactionFrequency
    is_active: bool = pydantic.Field()
    """
    Indicates whether the transaction stream is still live.
    """

    last_amount: TransactionStreamAmount
    last_date: dt.date = pydantic.Field()
    """
    The posted date of the latest transaction in the stream.
    """

    merchant_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The merchant associated with the transaction stream.
    """

    personal_finance_category: typing.Optional[PersonalFinanceCategory] = None
    status: TransactionStreamStatus
    stream_id: str = pydantic.Field()
    """
    A unique id for the stream
    """

    transaction_ids: typing.List[str] = pydantic.Field()
    """
    An array of Plaid transaction IDs belonging to the stream, sorted by posted date.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
