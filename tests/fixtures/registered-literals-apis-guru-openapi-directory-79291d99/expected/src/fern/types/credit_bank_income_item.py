

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_income_account import CreditBankIncomeAccount
from .credit_bank_income_source import CreditBankIncomeSource


class CreditBankIncomeItem(UniversalBaseModel):
    """
    The details and metadata for an end user's Item.
    """

    bank_income_accounts: typing.Optional[typing.List[CreditBankIncomeAccount]] = pydantic.Field(default=None)
    """
    The Item's accounts that have Bank Income data.
    """

    bank_income_sources: typing.Optional[typing.List[CreditBankIncomeSource]] = pydantic.Field(default=None)
    """
    The income sources for this Item. Each entry in the array is a single income source.
    """

    institution_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the institution associated with the Item.
    """

    institution_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the institution associated with the Item.
    """

    item_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for the Item.
    """

    last_updated_time: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The time when this Item's data was last retrieved from the financial institution.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
