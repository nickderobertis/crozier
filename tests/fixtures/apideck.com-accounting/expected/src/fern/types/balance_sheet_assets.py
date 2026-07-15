

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .balance_sheet_assets_current_assets import BalanceSheetAssetsCurrentAssets
from .balance_sheet_assets_fixed_assets import BalanceSheetAssetsFixedAssets


class BalanceSheetAssets(UniversalBaseModel):
    current_assets: BalanceSheetAssetsCurrentAssets
    fixed_assets: BalanceSheetAssetsFixedAssets
    total: float = pydantic.Field()
    """
    Total assets
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
