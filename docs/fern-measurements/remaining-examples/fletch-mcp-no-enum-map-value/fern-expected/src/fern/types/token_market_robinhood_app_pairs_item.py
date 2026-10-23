

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .token_market_robinhood_app_pairs_item_asset_currency import TokenMarketRobinhoodAppPairsItemAssetCurrency
from .token_market_robinhood_app_pairs_item_quote_currency import TokenMarketRobinhoodAppPairsItemQuoteCurrency
from .token_market_robinhood_app_pairs_item_tradability import TokenMarketRobinhoodAppPairsItemTradability
from .token_market_robinhood_app_pairs_item_tradability_by_account_type_value import (
    TokenMarketRobinhoodAppPairsItemTradabilityByAccountTypeValue,
)


class TokenMarketRobinhoodAppPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: TokenMarketRobinhoodAppPairsItemTradability
    tradability_by_account_type: typing.Dict[str, TokenMarketRobinhoodAppPairsItemTradabilityByAccountTypeValue]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: TokenMarketRobinhoodAppPairsItemAssetCurrency
    quote_currency: TokenMarketRobinhoodAppPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
