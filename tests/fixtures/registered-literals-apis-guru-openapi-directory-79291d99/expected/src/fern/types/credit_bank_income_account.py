

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_bank_income_account_type import CreditBankIncomeAccountType
from .depository_account_subtype import DepositoryAccountSubtype
from .owner import Owner


class CreditBankIncomeAccount(UniversalBaseModel):
    """
    The Item's bank accounts that have the selected data.
    """

    account_id: str = pydantic.Field()
    """
    Plaid's unique identifier for the account.
    """

    mask: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last 2-4 alphanumeric characters of an account's official account number.
    Note that the mask may be non-unique between an Item's accounts, and it may also not match the mask that the bank displays to the user.
    """

    name: str = pydantic.Field()
    """
    The name of the bank account.
    """

    official_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The official name of the bank account.
    """

    owners: typing.List[Owner] = pydantic.Field()
    """
    Data returned by the financial institution about the account owner or owners. Identity information is optional, so field may return an empty array.
    """

    subtype: DepositoryAccountSubtype
    type: CreditBankIncomeAccountType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
