

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_employment import CreditBankEmployment
from .credit_bank_income_account import CreditBankIncomeAccount


class CreditBankEmploymentItem(UniversalBaseModel):
    """
    The details and metadata for an end user's Item.
    """

    bank_employment_accounts: typing.List[CreditBankIncomeAccount] = pydantic.Field()
    """
    The Item's accounts that have Bank Employment data.
    """

    bank_employments: typing.List[CreditBankEmployment] = pydantic.Field()
    """
    The bank employment information for this Item. Each entry in the array is a different employer found.
    """

    institution_id: str = pydantic.Field()
    """
    The unique identifier of the institution associated with the Item.
    """

    institution_name: str = pydantic.Field()
    """
    The name of the institution associated with the Item.
    """

    item_id: str = pydantic.Field()
    """
    The unique identifier for the Item.
    """

    last_updated_time: dt.datetime = pydantic.Field()
    """
    The time when this Item's data was last retrieved from the financial institution, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (e.g. "2018-04-12T03:32:11Z").
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
