



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_app_catalog_request_status import GetAppCatalogRequestStatus
    from .get_app_catalog_response import GetAppCatalogResponse
    from .get_app_catalog_response_items_item import GetAppCatalogResponseItemsItem
    from .get_app_catalog_response_items_item_pairs_item import GetAppCatalogResponseItemsItemPairsItem
    from .get_app_catalog_response_items_item_pairs_item_asset_currency import (
        GetAppCatalogResponseItemsItemPairsItemAssetCurrency,
    )
    from .get_app_catalog_response_items_item_pairs_item_quote_currency import (
        GetAppCatalogResponseItemsItemPairsItemQuoteCurrency,
    )
    from .get_app_catalog_response_items_item_pairs_item_tradability import (
        GetAppCatalogResponseItemsItemPairsItemTradability,
    )
    from .get_app_catalog_response_items_item_pairs_item_tradability_by_account_type_value import (
        GetAppCatalogResponseItemsItemPairsItemTradabilityByAccountTypeValue,
    )
    from .get_app_catalog_response_items_item_status import GetAppCatalogResponseItemsItemStatus
    from .get_chains_chain_id_dex_pools_request_kind import GetChainsChainIdDexPoolsRequestKind
    from .get_chains_chain_id_dex_pools_request_sort import GetChainsChainIdDexPoolsRequestSort
    from .get_chains_chain_id_dex_pools_request_tier import GetChainsChainIdDexPoolsRequestTier
    from .get_chains_chain_id_dex_pools_request_venue import GetChainsChainIdDexPoolsRequestVenue
    from .get_chains_chain_id_dex_pools_response import GetChainsChainIdDexPoolsResponse
    from .get_chains_chain_id_dex_pools_response_discovery_item import GetChainsChainIdDexPoolsResponseDiscoveryItem
    from .get_chains_chain_id_dex_pools_response_pools_item import GetChainsChainIdDexPoolsResponsePoolsItem
    from .get_chains_chain_id_dex_pools_response_pools_item_depth_measure import (
        GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure,
    )
    from .get_chains_chain_id_dex_pools_response_pools_item_kind import GetChainsChainIdDexPoolsResponsePoolsItemKind
    from .get_chains_chain_id_dex_pools_response_pools_item_listing import (
        GetChainsChainIdDexPoolsResponsePoolsItemListing,
    )
    from .get_chains_chain_id_dex_pools_response_pools_item_quote_observation import (
        GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservation,
    )
    from .get_chains_chain_id_dex_pools_response_pools_item_quote_observation_parameters_value import (
        GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservationParametersValue,
    )
    from .get_chains_chain_id_dex_pools_response_pools_item_tier import GetChainsChainIdDexPoolsResponsePoolsItemTier
    from .get_chains_chain_id_dex_pools_response_pools_item_token import GetChainsChainIdDexPoolsResponsePoolsItemToken
    from .get_chains_chain_id_dex_pools_response_pools_item_trust import GetChainsChainIdDexPoolsResponsePoolsItemTrust
    from .get_chains_chain_id_dex_pools_response_pools_item_venue import GetChainsChainIdDexPoolsResponsePoolsItemVenue
    from .get_chains_chain_id_markets_filters_response import GetChainsChainIdMarketsFiltersResponse
    from .get_chains_chain_id_markets_filters_response_filters import GetChainsChainIdMarketsFiltersResponseFilters
    from .get_chains_chain_id_markets_filters_response_filters_activity import (
        GetChainsChainIdMarketsFiltersResponseFiltersActivity,
    )
    from .get_chains_chain_id_markets_filters_response_filters_activity_options_item import (
        GetChainsChainIdMarketsFiltersResponseFiltersActivityOptionsItem,
    )
    from .get_chains_chain_id_markets_filters_response_filters_data import (
        GetChainsChainIdMarketsFiltersResponseFiltersData,
    )
    from .get_chains_chain_id_markets_filters_response_filters_data_options_item import (
        GetChainsChainIdMarketsFiltersResponseFiltersDataOptionsItem,
    )
    from .get_chains_chain_id_markets_filters_response_filters_depth import (
        GetChainsChainIdMarketsFiltersResponseFiltersDepth,
    )
    from .get_chains_chain_id_markets_filters_response_filters_depth_options_item import (
        GetChainsChainIdMarketsFiltersResponseFiltersDepthOptionsItem,
    )
    from .get_chains_chain_id_markets_filters_response_filters_identity import (
        GetChainsChainIdMarketsFiltersResponseFiltersIdentity,
    )
    from .get_chains_chain_id_markets_filters_response_filters_identity_options_item import (
        GetChainsChainIdMarketsFiltersResponseFiltersIdentityOptionsItem,
    )
    from .get_chains_chain_id_markets_filters_response_filters_kind import (
        GetChainsChainIdMarketsFiltersResponseFiltersKind,
    )
    from .get_chains_chain_id_markets_filters_response_filters_kind_options_item import (
        GetChainsChainIdMarketsFiltersResponseFiltersKindOptionsItem,
    )
    from .get_chains_chain_id_markets_filters_response_filters_sort import (
        GetChainsChainIdMarketsFiltersResponseFiltersSort,
    )
    from .get_chains_chain_id_markets_filters_response_filters_sort_options_item import (
        GetChainsChainIdMarketsFiltersResponseFiltersSortOptionsItem,
    )
    from .get_chains_chain_id_markets_filters_response_filters_trust import (
        GetChainsChainIdMarketsFiltersResponseFiltersTrust,
    )
    from .get_chains_chain_id_markets_filters_response_filters_trust_options_item import (
        GetChainsChainIdMarketsFiltersResponseFiltersTrustOptionsItem,
    )
    from .get_chains_chain_id_markets_filters_response_min_volume_usd import (
        GetChainsChainIdMarketsFiltersResponseMinVolumeUsd,
    )
    from .get_chains_chain_id_markets_filters_response_presets_item import (
        GetChainsChainIdMarketsFiltersResponsePresetsItem,
    )
    from .get_chains_chain_id_markets_request_activity import GetChainsChainIdMarketsRequestActivity
    from .get_chains_chain_id_markets_request_data import GetChainsChainIdMarketsRequestData
    from .get_chains_chain_id_markets_request_depth import GetChainsChainIdMarketsRequestDepth
    from .get_chains_chain_id_markets_request_identity import GetChainsChainIdMarketsRequestIdentity
    from .get_chains_chain_id_markets_request_kind import GetChainsChainIdMarketsRequestKind
    from .get_chains_chain_id_markets_request_sort import GetChainsChainIdMarketsRequestSort
    from .get_chains_chain_id_markets_request_trust import GetChainsChainIdMarketsRequestTrust
    from .get_chains_chain_id_markets_response import GetChainsChainIdMarketsResponse
    from .get_chains_chain_id_markets_response_catalog import GetChainsChainIdMarketsResponseCatalog
    from .get_chains_chain_id_markets_response_catalog_matches_item import (
        GetChainsChainIdMarketsResponseCatalogMatchesItem,
    )
    from .get_chains_chain_id_markets_response_catalog_matches_item_status import (
        GetChainsChainIdMarketsResponseCatalogMatchesItemStatus,
    )
    from .get_chains_chain_id_markets_response_catalog_matches_item_status_match import (
        GetChainsChainIdMarketsResponseCatalogMatchesItemStatusMatch,
    )
    from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item import (
        GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItem,
    )
    from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_asset_currency import (
        GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemAssetCurrency,
    )
    from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_quote_currency import (
        GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemQuoteCurrency,
    )
    from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_tradability import (
        GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradability,
    )
    from .get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_tradability_by_account_type_value import (
        GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradabilityByAccountTypeValue,
    )
    from .get_chains_chain_id_markets_response_catalog_matches_item_status_status import (
        GetChainsChainIdMarketsResponseCatalogMatchesItemStatusStatus,
    )
    from .get_chains_chain_id_markets_response_catalog_pairs_item import GetChainsChainIdMarketsResponseCatalogPairsItem
    from .get_chains_chain_id_markets_response_catalog_pairs_item_asset_currency import (
        GetChainsChainIdMarketsResponseCatalogPairsItemAssetCurrency,
    )
    from .get_chains_chain_id_markets_response_catalog_pairs_item_quote_currency import (
        GetChainsChainIdMarketsResponseCatalogPairsItemQuoteCurrency,
    )
    from .get_chains_chain_id_markets_response_catalog_pairs_item_tradability import (
        GetChainsChainIdMarketsResponseCatalogPairsItemTradability,
    )
    from .get_chains_chain_id_markets_response_catalog_pairs_item_tradability_by_account_type_value import (
        GetChainsChainIdMarketsResponseCatalogPairsItemTradabilityByAccountTypeValue,
    )
    from .get_chains_chain_id_markets_response_items_item import GetChainsChainIdMarketsResponseItemsItem
    from .get_chains_chain_id_markets_response_items_item_alternatives_item import (
        GetChainsChainIdMarketsResponseItemsItemAlternativesItem,
    )
    from .get_chains_chain_id_markets_response_items_item_burned_raw import (
        GetChainsChainIdMarketsResponseItemsItemBurnedRaw,
    )
    from .get_chains_chain_id_markets_response_items_item_decimals import (
        GetChainsChainIdMarketsResponseItemsItemDecimals,
    )
    from .get_chains_chain_id_markets_response_items_item_holders import GetChainsChainIdMarketsResponseItemsItemHolders
    from .get_chains_chain_id_markets_response_items_item_market_cap_usd import (
        GetChainsChainIdMarketsResponseItemsItemMarketCapUsd,
    )
    from .get_chains_chain_id_markets_response_items_item_price_usd import (
        GetChainsChainIdMarketsResponseItemsItemPriceUsd,
    )
    from .get_chains_chain_id_markets_response_items_item_robinhood_app import (
        GetChainsChainIdMarketsResponseItemsItemRobinhoodApp,
    )
    from .get_chains_chain_id_markets_response_items_item_robinhood_app_match import (
        GetChainsChainIdMarketsResponseItemsItemRobinhoodAppMatch,
    )
    from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item import (
        GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItem,
    )
    from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_asset_currency import (
        GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemAssetCurrency,
    )
    from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_quote_currency import (
        GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemQuoteCurrency,
    )
    from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_tradability import (
        GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradability,
    )
    from .get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_tradability_by_account_type_value import (
        GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradabilityByAccountTypeValue,
    )
    from .get_chains_chain_id_markets_response_items_item_robinhood_app_status import (
        GetChainsChainIdMarketsResponseItemsItemRobinhoodAppStatus,
    )
    from .get_chains_chain_id_markets_response_items_item_selection import (
        GetChainsChainIdMarketsResponseItemsItemSelection,
    )
    from .get_chains_chain_id_markets_response_items_item_selection_status import (
        GetChainsChainIdMarketsResponseItemsItemSelectionStatus,
    )
    from .get_chains_chain_id_markets_response_items_item_stock_pairings_item import (
        GetChainsChainIdMarketsResponseItemsItemStockPairingsItem,
    )
    from .get_chains_chain_id_markets_response_items_item_stock_pairings_item_stock_verdict import (
        GetChainsChainIdMarketsResponseItemsItemStockPairingsItemStockVerdict,
    )
    from .get_chains_chain_id_markets_response_items_item_swaps24h import (
        GetChainsChainIdMarketsResponseItemsItemSwaps24H,
    )
    from .get_chains_chain_id_markets_response_items_item_total_supply_raw import (
        GetChainsChainIdMarketsResponseItemsItemTotalSupplyRaw,
    )
    from .get_chains_chain_id_markets_response_items_item_transactions24h import (
        GetChainsChainIdMarketsResponseItemsItemTransactions24H,
    )
    from .get_chains_chain_id_markets_response_items_item_trust import GetChainsChainIdMarketsResponseItemsItemTrust
    from .get_chains_chain_id_markets_response_items_item_v3quote_holdings_usd import (
        GetChainsChainIdMarketsResponseItemsItemV3QuoteHoldingsUsd,
    )
    from .get_chains_chain_id_markets_response_items_item_v4one_percent_depth_usd import (
        GetChainsChainIdMarketsResponseItemsItemV4OnePercentDepthUsd,
    )
    from .get_chains_chain_id_markets_response_items_item_volume_scope import (
        GetChainsChainIdMarketsResponseItemsItemVolumeScope,
    )
    from .get_chains_chain_id_markets_response_items_item_volume_usd24h import (
        GetChainsChainIdMarketsResponseItemsItemVolumeUsd24H,
    )
    from .get_chains_response import GetChainsResponse
    from .get_chains_response_chains_item import GetChainsResponseChainsItem
    from .get_chains_response_chains_item_network import GetChainsResponseChainsItemNetwork
    from .get_tokens_address_response import GetTokensAddressResponse
    from .get_tokens_address_response_impersonates import GetTokensAddressResponseImpersonates
    from .get_tokens_address_response_market import GetTokensAddressResponseMarket
    from .get_tokens_address_response_market_price_source import GetTokensAddressResponseMarketPriceSource
    from .get_tokens_address_response_reading import GetTokensAddressResponseReading
    from .get_tokens_address_response_reading_alternatives_item import GetTokensAddressResponseReadingAlternativesItem
    from .get_tokens_address_response_reading_burned_raw import GetTokensAddressResponseReadingBurnedRaw
    from .get_tokens_address_response_reading_decimals import GetTokensAddressResponseReadingDecimals
    from .get_tokens_address_response_reading_holders import GetTokensAddressResponseReadingHolders
    from .get_tokens_address_response_reading_market_cap_usd import GetTokensAddressResponseReadingMarketCapUsd
    from .get_tokens_address_response_reading_price_usd import GetTokensAddressResponseReadingPriceUsd
    from .get_tokens_address_response_reading_robinhood_app import GetTokensAddressResponseReadingRobinhoodApp
    from .get_tokens_address_response_reading_robinhood_app_match import (
        GetTokensAddressResponseReadingRobinhoodAppMatch,
    )
    from .get_tokens_address_response_reading_robinhood_app_pairs_item import (
        GetTokensAddressResponseReadingRobinhoodAppPairsItem,
    )
    from .get_tokens_address_response_reading_robinhood_app_pairs_item_asset_currency import (
        GetTokensAddressResponseReadingRobinhoodAppPairsItemAssetCurrency,
    )
    from .get_tokens_address_response_reading_robinhood_app_pairs_item_quote_currency import (
        GetTokensAddressResponseReadingRobinhoodAppPairsItemQuoteCurrency,
    )
    from .get_tokens_address_response_reading_robinhood_app_pairs_item_tradability import (
        GetTokensAddressResponseReadingRobinhoodAppPairsItemTradability,
    )
    from .get_tokens_address_response_reading_robinhood_app_status import (
        GetTokensAddressResponseReadingRobinhoodAppStatus,
    )
    from .get_tokens_address_response_reading_selection import GetTokensAddressResponseReadingSelection
    from .get_tokens_address_response_reading_selection_status import GetTokensAddressResponseReadingSelectionStatus
    from .get_tokens_address_response_reading_stock_pairings_item import (
        GetTokensAddressResponseReadingStockPairingsItem,
    )
    from .get_tokens_address_response_reading_stock_pairings_item_stock_verdict import (
        GetTokensAddressResponseReadingStockPairingsItemStockVerdict,
    )
    from .get_tokens_address_response_reading_swaps24h import GetTokensAddressResponseReadingSwaps24H
    from .get_tokens_address_response_reading_total_supply_raw import GetTokensAddressResponseReadingTotalSupplyRaw
    from .get_tokens_address_response_reading_transactions24h import GetTokensAddressResponseReadingTransactions24H
    from .get_tokens_address_response_reading_trust import GetTokensAddressResponseReadingTrust
    from .get_tokens_address_response_reading_v3quote_holdings_usd import (
        GetTokensAddressResponseReadingV3QuoteHoldingsUsd,
    )
    from .get_tokens_address_response_reading_v4one_percent_depth_usd import (
        GetTokensAddressResponseReadingV4OnePercentDepthUsd,
    )
    from .get_tokens_address_response_reading_volume_scope import GetTokensAddressResponseReadingVolumeScope
    from .get_tokens_address_response_reading_volume_usd24h import GetTokensAddressResponseReadingVolumeUsd24H
    from .get_tokens_address_response_source import GetTokensAddressResponseSource
    from .get_tokens_address_response_trust import GetTokensAddressResponseTrust
_dynamic_imports: typing.Dict[str, str] = {
    "GetAppCatalogRequestStatus": ".get_app_catalog_request_status",
    "GetAppCatalogResponse": ".get_app_catalog_response",
    "GetAppCatalogResponseItemsItem": ".get_app_catalog_response_items_item",
    "GetAppCatalogResponseItemsItemPairsItem": ".get_app_catalog_response_items_item_pairs_item",
    "GetAppCatalogResponseItemsItemPairsItemAssetCurrency": ".get_app_catalog_response_items_item_pairs_item_asset_currency",
    "GetAppCatalogResponseItemsItemPairsItemQuoteCurrency": ".get_app_catalog_response_items_item_pairs_item_quote_currency",
    "GetAppCatalogResponseItemsItemPairsItemTradability": ".get_app_catalog_response_items_item_pairs_item_tradability",
    "GetAppCatalogResponseItemsItemPairsItemTradabilityByAccountTypeValue": ".get_app_catalog_response_items_item_pairs_item_tradability_by_account_type_value",
    "GetAppCatalogResponseItemsItemStatus": ".get_app_catalog_response_items_item_status",
    "GetChainsChainIdDexPoolsRequestKind": ".get_chains_chain_id_dex_pools_request_kind",
    "GetChainsChainIdDexPoolsRequestSort": ".get_chains_chain_id_dex_pools_request_sort",
    "GetChainsChainIdDexPoolsRequestTier": ".get_chains_chain_id_dex_pools_request_tier",
    "GetChainsChainIdDexPoolsRequestVenue": ".get_chains_chain_id_dex_pools_request_venue",
    "GetChainsChainIdDexPoolsResponse": ".get_chains_chain_id_dex_pools_response",
    "GetChainsChainIdDexPoolsResponseDiscoveryItem": ".get_chains_chain_id_dex_pools_response_discovery_item",
    "GetChainsChainIdDexPoolsResponsePoolsItem": ".get_chains_chain_id_dex_pools_response_pools_item",
    "GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure": ".get_chains_chain_id_dex_pools_response_pools_item_depth_measure",
    "GetChainsChainIdDexPoolsResponsePoolsItemKind": ".get_chains_chain_id_dex_pools_response_pools_item_kind",
    "GetChainsChainIdDexPoolsResponsePoolsItemListing": ".get_chains_chain_id_dex_pools_response_pools_item_listing",
    "GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservation": ".get_chains_chain_id_dex_pools_response_pools_item_quote_observation",
    "GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservationParametersValue": ".get_chains_chain_id_dex_pools_response_pools_item_quote_observation_parameters_value",
    "GetChainsChainIdDexPoolsResponsePoolsItemTier": ".get_chains_chain_id_dex_pools_response_pools_item_tier",
    "GetChainsChainIdDexPoolsResponsePoolsItemToken": ".get_chains_chain_id_dex_pools_response_pools_item_token",
    "GetChainsChainIdDexPoolsResponsePoolsItemTrust": ".get_chains_chain_id_dex_pools_response_pools_item_trust",
    "GetChainsChainIdDexPoolsResponsePoolsItemVenue": ".get_chains_chain_id_dex_pools_response_pools_item_venue",
    "GetChainsChainIdMarketsFiltersResponse": ".get_chains_chain_id_markets_filters_response",
    "GetChainsChainIdMarketsFiltersResponseFilters": ".get_chains_chain_id_markets_filters_response_filters",
    "GetChainsChainIdMarketsFiltersResponseFiltersActivity": ".get_chains_chain_id_markets_filters_response_filters_activity",
    "GetChainsChainIdMarketsFiltersResponseFiltersActivityOptionsItem": ".get_chains_chain_id_markets_filters_response_filters_activity_options_item",
    "GetChainsChainIdMarketsFiltersResponseFiltersData": ".get_chains_chain_id_markets_filters_response_filters_data",
    "GetChainsChainIdMarketsFiltersResponseFiltersDataOptionsItem": ".get_chains_chain_id_markets_filters_response_filters_data_options_item",
    "GetChainsChainIdMarketsFiltersResponseFiltersDepth": ".get_chains_chain_id_markets_filters_response_filters_depth",
    "GetChainsChainIdMarketsFiltersResponseFiltersDepthOptionsItem": ".get_chains_chain_id_markets_filters_response_filters_depth_options_item",
    "GetChainsChainIdMarketsFiltersResponseFiltersIdentity": ".get_chains_chain_id_markets_filters_response_filters_identity",
    "GetChainsChainIdMarketsFiltersResponseFiltersIdentityOptionsItem": ".get_chains_chain_id_markets_filters_response_filters_identity_options_item",
    "GetChainsChainIdMarketsFiltersResponseFiltersKind": ".get_chains_chain_id_markets_filters_response_filters_kind",
    "GetChainsChainIdMarketsFiltersResponseFiltersKindOptionsItem": ".get_chains_chain_id_markets_filters_response_filters_kind_options_item",
    "GetChainsChainIdMarketsFiltersResponseFiltersSort": ".get_chains_chain_id_markets_filters_response_filters_sort",
    "GetChainsChainIdMarketsFiltersResponseFiltersSortOptionsItem": ".get_chains_chain_id_markets_filters_response_filters_sort_options_item",
    "GetChainsChainIdMarketsFiltersResponseFiltersTrust": ".get_chains_chain_id_markets_filters_response_filters_trust",
    "GetChainsChainIdMarketsFiltersResponseFiltersTrustOptionsItem": ".get_chains_chain_id_markets_filters_response_filters_trust_options_item",
    "GetChainsChainIdMarketsFiltersResponseMinVolumeUsd": ".get_chains_chain_id_markets_filters_response_min_volume_usd",
    "GetChainsChainIdMarketsFiltersResponsePresetsItem": ".get_chains_chain_id_markets_filters_response_presets_item",
    "GetChainsChainIdMarketsRequestActivity": ".get_chains_chain_id_markets_request_activity",
    "GetChainsChainIdMarketsRequestData": ".get_chains_chain_id_markets_request_data",
    "GetChainsChainIdMarketsRequestDepth": ".get_chains_chain_id_markets_request_depth",
    "GetChainsChainIdMarketsRequestIdentity": ".get_chains_chain_id_markets_request_identity",
    "GetChainsChainIdMarketsRequestKind": ".get_chains_chain_id_markets_request_kind",
    "GetChainsChainIdMarketsRequestSort": ".get_chains_chain_id_markets_request_sort",
    "GetChainsChainIdMarketsRequestTrust": ".get_chains_chain_id_markets_request_trust",
    "GetChainsChainIdMarketsResponse": ".get_chains_chain_id_markets_response",
    "GetChainsChainIdMarketsResponseCatalog": ".get_chains_chain_id_markets_response_catalog",
    "GetChainsChainIdMarketsResponseCatalogMatchesItem": ".get_chains_chain_id_markets_response_catalog_matches_item",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatus": ".get_chains_chain_id_markets_response_catalog_matches_item_status",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusMatch": ".get_chains_chain_id_markets_response_catalog_matches_item_status_match",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItem": ".get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemAssetCurrency": ".get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_asset_currency",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemQuoteCurrency": ".get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_quote_currency",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradability": ".get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_tradability",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradabilityByAccountTypeValue": ".get_chains_chain_id_markets_response_catalog_matches_item_status_pairs_item_tradability_by_account_type_value",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusStatus": ".get_chains_chain_id_markets_response_catalog_matches_item_status_status",
    "GetChainsChainIdMarketsResponseCatalogPairsItem": ".get_chains_chain_id_markets_response_catalog_pairs_item",
    "GetChainsChainIdMarketsResponseCatalogPairsItemAssetCurrency": ".get_chains_chain_id_markets_response_catalog_pairs_item_asset_currency",
    "GetChainsChainIdMarketsResponseCatalogPairsItemQuoteCurrency": ".get_chains_chain_id_markets_response_catalog_pairs_item_quote_currency",
    "GetChainsChainIdMarketsResponseCatalogPairsItemTradability": ".get_chains_chain_id_markets_response_catalog_pairs_item_tradability",
    "GetChainsChainIdMarketsResponseCatalogPairsItemTradabilityByAccountTypeValue": ".get_chains_chain_id_markets_response_catalog_pairs_item_tradability_by_account_type_value",
    "GetChainsChainIdMarketsResponseItemsItem": ".get_chains_chain_id_markets_response_items_item",
    "GetChainsChainIdMarketsResponseItemsItemAlternativesItem": ".get_chains_chain_id_markets_response_items_item_alternatives_item",
    "GetChainsChainIdMarketsResponseItemsItemBurnedRaw": ".get_chains_chain_id_markets_response_items_item_burned_raw",
    "GetChainsChainIdMarketsResponseItemsItemDecimals": ".get_chains_chain_id_markets_response_items_item_decimals",
    "GetChainsChainIdMarketsResponseItemsItemHolders": ".get_chains_chain_id_markets_response_items_item_holders",
    "GetChainsChainIdMarketsResponseItemsItemMarketCapUsd": ".get_chains_chain_id_markets_response_items_item_market_cap_usd",
    "GetChainsChainIdMarketsResponseItemsItemPriceUsd": ".get_chains_chain_id_markets_response_items_item_price_usd",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodApp": ".get_chains_chain_id_markets_response_items_item_robinhood_app",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppMatch": ".get_chains_chain_id_markets_response_items_item_robinhood_app_match",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItem": ".get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemAssetCurrency": ".get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_asset_currency",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemQuoteCurrency": ".get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_quote_currency",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradability": ".get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_tradability",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradabilityByAccountTypeValue": ".get_chains_chain_id_markets_response_items_item_robinhood_app_pairs_item_tradability_by_account_type_value",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppStatus": ".get_chains_chain_id_markets_response_items_item_robinhood_app_status",
    "GetChainsChainIdMarketsResponseItemsItemSelection": ".get_chains_chain_id_markets_response_items_item_selection",
    "GetChainsChainIdMarketsResponseItemsItemSelectionStatus": ".get_chains_chain_id_markets_response_items_item_selection_status",
    "GetChainsChainIdMarketsResponseItemsItemStockPairingsItem": ".get_chains_chain_id_markets_response_items_item_stock_pairings_item",
    "GetChainsChainIdMarketsResponseItemsItemStockPairingsItemStockVerdict": ".get_chains_chain_id_markets_response_items_item_stock_pairings_item_stock_verdict",
    "GetChainsChainIdMarketsResponseItemsItemSwaps24H": ".get_chains_chain_id_markets_response_items_item_swaps24h",
    "GetChainsChainIdMarketsResponseItemsItemTotalSupplyRaw": ".get_chains_chain_id_markets_response_items_item_total_supply_raw",
    "GetChainsChainIdMarketsResponseItemsItemTransactions24H": ".get_chains_chain_id_markets_response_items_item_transactions24h",
    "GetChainsChainIdMarketsResponseItemsItemTrust": ".get_chains_chain_id_markets_response_items_item_trust",
    "GetChainsChainIdMarketsResponseItemsItemV3QuoteHoldingsUsd": ".get_chains_chain_id_markets_response_items_item_v3quote_holdings_usd",
    "GetChainsChainIdMarketsResponseItemsItemV4OnePercentDepthUsd": ".get_chains_chain_id_markets_response_items_item_v4one_percent_depth_usd",
    "GetChainsChainIdMarketsResponseItemsItemVolumeScope": ".get_chains_chain_id_markets_response_items_item_volume_scope",
    "GetChainsChainIdMarketsResponseItemsItemVolumeUsd24H": ".get_chains_chain_id_markets_response_items_item_volume_usd24h",
    "GetChainsResponse": ".get_chains_response",
    "GetChainsResponseChainsItem": ".get_chains_response_chains_item",
    "GetChainsResponseChainsItemNetwork": ".get_chains_response_chains_item_network",
    "GetTokensAddressResponse": ".get_tokens_address_response",
    "GetTokensAddressResponseImpersonates": ".get_tokens_address_response_impersonates",
    "GetTokensAddressResponseMarket": ".get_tokens_address_response_market",
    "GetTokensAddressResponseMarketPriceSource": ".get_tokens_address_response_market_price_source",
    "GetTokensAddressResponseReading": ".get_tokens_address_response_reading",
    "GetTokensAddressResponseReadingAlternativesItem": ".get_tokens_address_response_reading_alternatives_item",
    "GetTokensAddressResponseReadingBurnedRaw": ".get_tokens_address_response_reading_burned_raw",
    "GetTokensAddressResponseReadingDecimals": ".get_tokens_address_response_reading_decimals",
    "GetTokensAddressResponseReadingHolders": ".get_tokens_address_response_reading_holders",
    "GetTokensAddressResponseReadingMarketCapUsd": ".get_tokens_address_response_reading_market_cap_usd",
    "GetTokensAddressResponseReadingPriceUsd": ".get_tokens_address_response_reading_price_usd",
    "GetTokensAddressResponseReadingRobinhoodApp": ".get_tokens_address_response_reading_robinhood_app",
    "GetTokensAddressResponseReadingRobinhoodAppMatch": ".get_tokens_address_response_reading_robinhood_app_match",
    "GetTokensAddressResponseReadingRobinhoodAppPairsItem": ".get_tokens_address_response_reading_robinhood_app_pairs_item",
    "GetTokensAddressResponseReadingRobinhoodAppPairsItemAssetCurrency": ".get_tokens_address_response_reading_robinhood_app_pairs_item_asset_currency",
    "GetTokensAddressResponseReadingRobinhoodAppPairsItemQuoteCurrency": ".get_tokens_address_response_reading_robinhood_app_pairs_item_quote_currency",
    "GetTokensAddressResponseReadingRobinhoodAppPairsItemTradability": ".get_tokens_address_response_reading_robinhood_app_pairs_item_tradability",
    "GetTokensAddressResponseReadingRobinhoodAppStatus": ".get_tokens_address_response_reading_robinhood_app_status",
    "GetTokensAddressResponseReadingSelection": ".get_tokens_address_response_reading_selection",
    "GetTokensAddressResponseReadingSelectionStatus": ".get_tokens_address_response_reading_selection_status",
    "GetTokensAddressResponseReadingStockPairingsItem": ".get_tokens_address_response_reading_stock_pairings_item",
    "GetTokensAddressResponseReadingStockPairingsItemStockVerdict": ".get_tokens_address_response_reading_stock_pairings_item_stock_verdict",
    "GetTokensAddressResponseReadingSwaps24H": ".get_tokens_address_response_reading_swaps24h",
    "GetTokensAddressResponseReadingTotalSupplyRaw": ".get_tokens_address_response_reading_total_supply_raw",
    "GetTokensAddressResponseReadingTransactions24H": ".get_tokens_address_response_reading_transactions24h",
    "GetTokensAddressResponseReadingTrust": ".get_tokens_address_response_reading_trust",
    "GetTokensAddressResponseReadingV3QuoteHoldingsUsd": ".get_tokens_address_response_reading_v3quote_holdings_usd",
    "GetTokensAddressResponseReadingV4OnePercentDepthUsd": ".get_tokens_address_response_reading_v4one_percent_depth_usd",
    "GetTokensAddressResponseReadingVolumeScope": ".get_tokens_address_response_reading_volume_scope",
    "GetTokensAddressResponseReadingVolumeUsd24H": ".get_tokens_address_response_reading_volume_usd24h",
    "GetTokensAddressResponseSource": ".get_tokens_address_response_source",
    "GetTokensAddressResponseTrust": ".get_tokens_address_response_trust",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "GetAppCatalogRequestStatus",
    "GetAppCatalogResponse",
    "GetAppCatalogResponseItemsItem",
    "GetAppCatalogResponseItemsItemPairsItem",
    "GetAppCatalogResponseItemsItemPairsItemAssetCurrency",
    "GetAppCatalogResponseItemsItemPairsItemQuoteCurrency",
    "GetAppCatalogResponseItemsItemPairsItemTradability",
    "GetAppCatalogResponseItemsItemPairsItemTradabilityByAccountTypeValue",
    "GetAppCatalogResponseItemsItemStatus",
    "GetChainsChainIdDexPoolsRequestKind",
    "GetChainsChainIdDexPoolsRequestSort",
    "GetChainsChainIdDexPoolsRequestTier",
    "GetChainsChainIdDexPoolsRequestVenue",
    "GetChainsChainIdDexPoolsResponse",
    "GetChainsChainIdDexPoolsResponseDiscoveryItem",
    "GetChainsChainIdDexPoolsResponsePoolsItem",
    "GetChainsChainIdDexPoolsResponsePoolsItemDepthMeasure",
    "GetChainsChainIdDexPoolsResponsePoolsItemKind",
    "GetChainsChainIdDexPoolsResponsePoolsItemListing",
    "GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservation",
    "GetChainsChainIdDexPoolsResponsePoolsItemQuoteObservationParametersValue",
    "GetChainsChainIdDexPoolsResponsePoolsItemTier",
    "GetChainsChainIdDexPoolsResponsePoolsItemToken",
    "GetChainsChainIdDexPoolsResponsePoolsItemTrust",
    "GetChainsChainIdDexPoolsResponsePoolsItemVenue",
    "GetChainsChainIdMarketsFiltersResponse",
    "GetChainsChainIdMarketsFiltersResponseFilters",
    "GetChainsChainIdMarketsFiltersResponseFiltersActivity",
    "GetChainsChainIdMarketsFiltersResponseFiltersActivityOptionsItem",
    "GetChainsChainIdMarketsFiltersResponseFiltersData",
    "GetChainsChainIdMarketsFiltersResponseFiltersDataOptionsItem",
    "GetChainsChainIdMarketsFiltersResponseFiltersDepth",
    "GetChainsChainIdMarketsFiltersResponseFiltersDepthOptionsItem",
    "GetChainsChainIdMarketsFiltersResponseFiltersIdentity",
    "GetChainsChainIdMarketsFiltersResponseFiltersIdentityOptionsItem",
    "GetChainsChainIdMarketsFiltersResponseFiltersKind",
    "GetChainsChainIdMarketsFiltersResponseFiltersKindOptionsItem",
    "GetChainsChainIdMarketsFiltersResponseFiltersSort",
    "GetChainsChainIdMarketsFiltersResponseFiltersSortOptionsItem",
    "GetChainsChainIdMarketsFiltersResponseFiltersTrust",
    "GetChainsChainIdMarketsFiltersResponseFiltersTrustOptionsItem",
    "GetChainsChainIdMarketsFiltersResponseMinVolumeUsd",
    "GetChainsChainIdMarketsFiltersResponsePresetsItem",
    "GetChainsChainIdMarketsRequestActivity",
    "GetChainsChainIdMarketsRequestData",
    "GetChainsChainIdMarketsRequestDepth",
    "GetChainsChainIdMarketsRequestIdentity",
    "GetChainsChainIdMarketsRequestKind",
    "GetChainsChainIdMarketsRequestSort",
    "GetChainsChainIdMarketsRequestTrust",
    "GetChainsChainIdMarketsResponse",
    "GetChainsChainIdMarketsResponseCatalog",
    "GetChainsChainIdMarketsResponseCatalogMatchesItem",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatus",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusMatch",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItem",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemAssetCurrency",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemQuoteCurrency",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradability",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusPairsItemTradabilityByAccountTypeValue",
    "GetChainsChainIdMarketsResponseCatalogMatchesItemStatusStatus",
    "GetChainsChainIdMarketsResponseCatalogPairsItem",
    "GetChainsChainIdMarketsResponseCatalogPairsItemAssetCurrency",
    "GetChainsChainIdMarketsResponseCatalogPairsItemQuoteCurrency",
    "GetChainsChainIdMarketsResponseCatalogPairsItemTradability",
    "GetChainsChainIdMarketsResponseCatalogPairsItemTradabilityByAccountTypeValue",
    "GetChainsChainIdMarketsResponseItemsItem",
    "GetChainsChainIdMarketsResponseItemsItemAlternativesItem",
    "GetChainsChainIdMarketsResponseItemsItemBurnedRaw",
    "GetChainsChainIdMarketsResponseItemsItemDecimals",
    "GetChainsChainIdMarketsResponseItemsItemHolders",
    "GetChainsChainIdMarketsResponseItemsItemMarketCapUsd",
    "GetChainsChainIdMarketsResponseItemsItemPriceUsd",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodApp",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppMatch",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItem",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemAssetCurrency",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemQuoteCurrency",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradability",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppPairsItemTradabilityByAccountTypeValue",
    "GetChainsChainIdMarketsResponseItemsItemRobinhoodAppStatus",
    "GetChainsChainIdMarketsResponseItemsItemSelection",
    "GetChainsChainIdMarketsResponseItemsItemSelectionStatus",
    "GetChainsChainIdMarketsResponseItemsItemStockPairingsItem",
    "GetChainsChainIdMarketsResponseItemsItemStockPairingsItemStockVerdict",
    "GetChainsChainIdMarketsResponseItemsItemSwaps24H",
    "GetChainsChainIdMarketsResponseItemsItemTotalSupplyRaw",
    "GetChainsChainIdMarketsResponseItemsItemTransactions24H",
    "GetChainsChainIdMarketsResponseItemsItemTrust",
    "GetChainsChainIdMarketsResponseItemsItemV3QuoteHoldingsUsd",
    "GetChainsChainIdMarketsResponseItemsItemV4OnePercentDepthUsd",
    "GetChainsChainIdMarketsResponseItemsItemVolumeScope",
    "GetChainsChainIdMarketsResponseItemsItemVolumeUsd24H",
    "GetChainsResponse",
    "GetChainsResponseChainsItem",
    "GetChainsResponseChainsItemNetwork",
    "GetTokensAddressResponse",
    "GetTokensAddressResponseImpersonates",
    "GetTokensAddressResponseMarket",
    "GetTokensAddressResponseMarketPriceSource",
    "GetTokensAddressResponseReading",
    "GetTokensAddressResponseReadingAlternativesItem",
    "GetTokensAddressResponseReadingBurnedRaw",
    "GetTokensAddressResponseReadingDecimals",
    "GetTokensAddressResponseReadingHolders",
    "GetTokensAddressResponseReadingMarketCapUsd",
    "GetTokensAddressResponseReadingPriceUsd",
    "GetTokensAddressResponseReadingRobinhoodApp",
    "GetTokensAddressResponseReadingRobinhoodAppMatch",
    "GetTokensAddressResponseReadingRobinhoodAppPairsItem",
    "GetTokensAddressResponseReadingRobinhoodAppPairsItemAssetCurrency",
    "GetTokensAddressResponseReadingRobinhoodAppPairsItemQuoteCurrency",
    "GetTokensAddressResponseReadingRobinhoodAppPairsItemTradability",
    "GetTokensAddressResponseReadingRobinhoodAppStatus",
    "GetTokensAddressResponseReadingSelection",
    "GetTokensAddressResponseReadingSelectionStatus",
    "GetTokensAddressResponseReadingStockPairingsItem",
    "GetTokensAddressResponseReadingStockPairingsItemStockVerdict",
    "GetTokensAddressResponseReadingSwaps24H",
    "GetTokensAddressResponseReadingTotalSupplyRaw",
    "GetTokensAddressResponseReadingTransactions24H",
    "GetTokensAddressResponseReadingTrust",
    "GetTokensAddressResponseReadingV3QuoteHoldingsUsd",
    "GetTokensAddressResponseReadingV4OnePercentDepthUsd",
    "GetTokensAddressResponseReadingVolumeScope",
    "GetTokensAddressResponseReadingVolumeUsd24H",
    "GetTokensAddressResponseSource",
    "GetTokensAddressResponseTrust",
]
