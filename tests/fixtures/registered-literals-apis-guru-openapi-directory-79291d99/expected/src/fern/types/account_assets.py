

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .account_base import AccountBase
from .asset_report_transaction import AssetReportTransaction
from .historical_balance import HistoricalBalance
from .owner import Owner
from .ownership_type import OwnershipType


class AccountAssets(AccountBase):
    """
    Asset information about an account
    """

    days_available: float = pydantic.Field()
    """
    The duration of transaction history available for this Item, typically defined as the time since the date of the earliest transaction in that account. Only returned by Assets endpoints.
    """

    historical_balances: typing.List[HistoricalBalance] = pydantic.Field()
    """
    Calculated data about the historical balances on the account. Only returned by Assets endpoints and currently not supported by `brokerage` or `investment` accounts.
    """

    owners: typing.List[Owner] = pydantic.Field()
    """
    Data returned by the financial institution about the account owner or owners. Only returned by Identity or Assets endpoints. For business accounts, the name reported may be either the name of the individual or the name of the business, depending on the institution. Multiple owners on a single account will be represented in the same `owner` object, not in multiple owner objects within the array. In API versions 2018-05-22 and earlier, the `owners` object is not returned, and instead identity information is returned in the top level `identity` object. For more details, see [Plaid API versioning](https://plaid.com/docs/api/versioning/#version-2019-05-29)
    """

    ownership_type: typing.Optional[OwnershipType] = None
    transactions: typing.List[AssetReportTransaction] = pydantic.Field()
    """
    Transaction history associated with the account. Only returned by Assets endpoints. Transaction history returned by endpoints such as `/transactions/get` or `/investments/transactions/get` will be returned in the top-level `transactions` field instead.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
