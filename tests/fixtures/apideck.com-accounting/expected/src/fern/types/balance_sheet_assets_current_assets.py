

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .balance_sheet_assets_current_assets_accounts_item import BalanceSheetAssetsCurrentAssetsAccountsItem


class BalanceSheetAssetsCurrentAssets(UniversalBaseModel):
    accounts: typing.List[BalanceSheetAssetsCurrentAssetsAccountsItem]
    total: float = pydantic.Field()
    """
    Total current assets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
