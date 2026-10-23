

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .service_unavailable_error_body_items_item_pairs_item_asset_currency import (
    ServiceUnavailableErrorBodyItemsItemPairsItemAssetCurrency,
)
from .service_unavailable_error_body_items_item_pairs_item_quote_currency import (
    ServiceUnavailableErrorBodyItemsItemPairsItemQuoteCurrency,
)
from .service_unavailable_error_body_items_item_pairs_item_tradability import (
    ServiceUnavailableErrorBodyItemsItemPairsItemTradability,
)
from .service_unavailable_error_body_items_item_pairs_item_tradability_by_account_type_value import (
    ServiceUnavailableErrorBodyItemsItemPairsItemTradabilityByAccountTypeValue,
)


class ServiceUnavailableErrorBodyItemsItemPairsItem(UniversalBaseModel):
    id: str
    symbol: str
    display_only: bool
    tradability: ServiceUnavailableErrorBodyItemsItemPairsItemTradability
    tradability_by_account_type: typing.Dict[
        str, ServiceUnavailableErrorBodyItemsItemPairsItemTradabilityByAccountTypeValue
    ]
    is_stablecoin: bool
    min_order_size: str
    max_order_size: str
    asset_currency: ServiceUnavailableErrorBodyItemsItemPairsItemAssetCurrency
    quote_currency: ServiceUnavailableErrorBodyItemsItemPairsItemQuoteCurrency

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
