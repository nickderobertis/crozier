

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransactionOverride(UniversalBaseModel):
    """
    Data to populate as test transaction data. If not specified, random transactions will be generated instead.
    """

    amount: float = pydantic.Field()
    """
    The transaction amount. Can be negative.
    """

    currency: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ISO-4217 format currency code for the transaction.
    """

    date_posted: dt.date = pydantic.Field()
    """
    The date the transaction posted, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Posted dates in the past or present will result in posted transactions; posted dates in the future will result in pending transactions.
    """

    date_transacted: dt.date = pydantic.Field()
    """
    The date of the transaction, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) (YYYY-MM-DD) format. Transactions in Sandbox will move from pending to posted once their transaction date has been reached. If a `date_transacted` is not provided by the institution, a transaction date may be available in the [`authorized_date`](https://plaid.com/docs/api/products/transactions/#transactions-get-response-transactions-authorized-date) field.
    """

    description: str = pydantic.Field()
    """
    The transaction description.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
