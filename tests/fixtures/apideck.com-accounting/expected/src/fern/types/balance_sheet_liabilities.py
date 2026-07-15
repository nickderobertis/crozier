

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .balance_sheet_liabilities_accounts_item import BalanceSheetLiabilitiesAccountsItem


class BalanceSheetLiabilities(UniversalBaseModel):
    accounts: typing.List[BalanceSheetLiabilitiesAccountsItem]
    total: float = pydantic.Field()
    """
    Total liabilities
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
