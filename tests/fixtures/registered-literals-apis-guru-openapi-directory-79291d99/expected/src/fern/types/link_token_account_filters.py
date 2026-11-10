

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .credit_filter import CreditFilter
from .depository_filter import DepositoryFilter
from .investment_filter import InvestmentFilter
from .loan_filter import LoanFilter


class LinkTokenAccountFilters(UniversalBaseModel):
    """
    By default, Link will provide limited account filtering: it will only display Institutions that are compatible with all products supplied in the `products` parameter of `/link/token/create`, and, if `auth` is specified in the `products` array, will also filter out accounts other than `checking` and `savings` accounts on the Account Select pane. You can further limit the accounts shown in Link by using `account_filters` to specify the account subtypes to be shown in Link. Only the specified subtypes will be shown. This filtering applies to both the Account Select view (if enabled) and the Institution Select view. Institutions that do not support the selected subtypes will be omitted from Link. To indicate that all subtypes should be shown, use the value `"all"`. If the `account_filters` filter is used, any account type for which a filter is not specified will be entirely omitted from Link. For a full list of valid types and subtypes, see the [Account schema](https://plaid.com/docs/api/accounts#account-type-schema).

    For institutions using OAuth, the filter will not affect the list of accounts shown by the bank in the OAuth window.
    """

    credit: typing.Optional[CreditFilter] = None
    depository: typing.Optional[DepositoryFilter] = None
    investment: typing.Optional[InvestmentFilter] = None
    loan: typing.Optional[LoanFilter] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
