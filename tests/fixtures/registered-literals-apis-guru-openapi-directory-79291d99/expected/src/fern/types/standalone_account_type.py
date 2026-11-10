

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_account import CreditAccount
from .depository_account import DepositoryAccount
from .investment_account_subtype_standalone import InvestmentAccountSubtypeStandalone
from .loan_account import LoanAccount


class StandaloneAccountType(UniversalBaseModel):
    """
    The schema below describes the various `types` and corresponding `subtypes` that Plaid recognizes and reports for financial institution accounts.
    """

    credit: CreditAccount
    depository: DepositoryAccount
    investment: InvestmentAccountSubtypeStandalone
    loan: LoanAccount
    other: str = pydantic.Field()
    """
    Other or unknown account type. Supported products for `other` accounts are: Balance, Transactions, Identity, and Assets.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
