

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_employer import CreditBankEmployer


class CreditBankEmployment(UniversalBaseModel):
    """
    Detailed information for the bank employment.
    """

    account_id: str = pydantic.Field()
    """
    Plaid's unique identifier for the account.
    """

    bank_employment_id: str = pydantic.Field()
    """
    A unique identifier for the bank employment.
    """

    earliest_deposit_date: dt.date = pydantic.Field()
    """
    The date of the earliest deposit from this employer from within the period of the days requested.
    """

    employer: CreditBankEmployer
    latest_deposit_date: dt.date = pydantic.Field()
    """
    The date of the most recent deposit from this employer.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
