

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TransactionData(UniversalBaseModel):
    """
    Information about the matched direct deposit transaction used to verify a user's payroll information.
    """

    account_id: str = pydantic.Field()
    """
    A unique identifier for the end user's account.
    """

    amount: float = pydantic.Field()
    """
    The amount of the transaction.
    """

    date: dt.date = pydantic.Field()
    """
    The date of the transaction, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format ("yyyy-mm-dd").
    """

    description: str = pydantic.Field()
    """
    The description of the transaction.
    """

    transaction_id: str = pydantic.Field()
    """
    A unique identifier for the transaction.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
