

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_tokens_address_response_reading_robinhood_app_pairs_item_asset_currency import (
    GetTokensAddressResponseReadingRobinhoodAppPairsItemAssetCurrency,
)
from .get_tokens_address_response_reading_robinhood_app_pairs_item_quote_currency import (
    GetTokensAddressResponseReadingRobinhoodAppPairsItemQuoteCurrency,
)
from .get_tokens_address_response_reading_robinhood_app_pairs_item_tradability import (
    GetTokensAddressResponseReadingRobinhoodAppPairsItemTradability,
)
from .get_tokens_address_response_reading_robinhood_app_pairs_item_tradability_by_account_type_value import (
    GetTokensAddressResponseReadingRobinhoodAppPairsItemTradabilityByAccountTypeValue,
)


class GetTokensAddressResponseReadingRobinhoodAppPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: GetTokensAddressResponseReadingRobinhoodAppPairsItemTradability
    tradability_by_account_type: typing.Dict[
        str, GetTokensAddressResponseReadingRobinhoodAppPairsItemTradabilityByAccountTypeValue
    ]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: GetTokensAddressResponseReadingRobinhoodAppPairsItemAssetCurrency
    quote_currency: GetTokensAddressResponseReadingRobinhoodAppPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
