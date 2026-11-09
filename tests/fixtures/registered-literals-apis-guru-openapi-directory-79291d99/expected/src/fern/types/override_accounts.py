

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_subtype import AccountSubtype
from .holdings_override import HoldingsOverride
from .income_override import IncomeOverride
from .inflow_model import InflowModel
from .investments_transactions_override import InvestmentsTransactionsOverride
from .liability_override import LiabilityOverride
from .meta import Meta
from .numbers import Numbers
from .override_account_type import OverrideAccountType
from .owner_override import OwnerOverride
from .transaction_override import TransactionOverride


class OverrideAccounts(UniversalBaseModel):
    """
    Data to use to set values of test accounts. Some values cannot be specified in the schema and will instead will be calculated from other test data in order to achieve more consistent, realistic test data.
    """

    currency: str = pydantic.Field()
    """
    ISO-4217 currency code. If provided, the account will be denominated in the given currency. Transactions will also be in this currency by default.
    """

    force_available_balance: float = pydantic.Field()
    """
    If provided, the account will always have this amount as its  available balance, regardless of current balance or changes in transactions over time.
    """

    holdings: typing.Optional[HoldingsOverride] = None
    identity: OwnerOverride
    income: typing.Optional[IncomeOverride] = None
    inflow_model: InflowModel
    investment_transactions: typing.Optional[InvestmentsTransactionsOverride] = None
    liability: LiabilityOverride
    meta: Meta
    numbers: Numbers
    starting_balance: float = pydantic.Field()
    """
    If provided, the account will start with this amount as the current balance.
    """

    subtype: typing.Optional[AccountSubtype] = None
    transactions: typing.List[TransactionOverride] = pydantic.Field()
    """
    Specify the list of transactions on the account.
    """

    type: OverrideAccountType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
