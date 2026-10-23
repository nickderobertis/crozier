



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .app_catalog_page import AppCatalogPage
    from .app_catalog_page_items_item import AppCatalogPageItemsItem
    from .app_catalog_page_items_item_pairs_item import AppCatalogPageItemsItemPairsItem
    from .app_catalog_page_items_item_pairs_item_asset_currency import AppCatalogPageItemsItemPairsItemAssetCurrency
    from .app_catalog_page_items_item_pairs_item_quote_currency import AppCatalogPageItemsItemPairsItemQuoteCurrency
    from .app_catalog_page_items_item_pairs_item_tradability import AppCatalogPageItemsItemPairsItemTradability
    from .app_catalog_page_items_item_pairs_item_tradability_by_account_type_value import (
        AppCatalogPageItemsItemPairsItemTradabilityByAccountTypeValue,
    )
    from .app_catalog_page_items_item_status import AppCatalogPageItemsItemStatus
    from .app_catalog_status import AppCatalogStatus
    from .app_catalog_status_match import AppCatalogStatusMatch
    from .app_catalog_status_pairs_item import AppCatalogStatusPairsItem
    from .app_catalog_status_pairs_item_asset_currency import AppCatalogStatusPairsItemAssetCurrency
    from .app_catalog_status_pairs_item_quote_currency import AppCatalogStatusPairsItemQuoteCurrency
    from .app_catalog_status_pairs_item_tradability import AppCatalogStatusPairsItemTradability
    from .app_catalog_status_pairs_item_tradability_by_account_type_value import (
        AppCatalogStatusPairsItemTradabilityByAccountTypeValue,
    )
    from .app_catalog_status_status import AppCatalogStatusStatus
    from .asset import Asset
    from .asset_asset_type import AssetAssetType
    from .authority_event import AuthorityEvent
    from .bad_request_error_body import BadRequestErrorBody
    from .chain import Chain
    from .chain_network import ChainNetwork
    from .error import Error
    from .forbidden_error_body import ForbiddenErrorBody
    from .market_selection import MarketSelection
    from .market_selection_status import MarketSelectionStatus
    from .metric_observation import MetricObservation
    from .metric_observation_coverage import MetricObservationCoverage
    from .metric_observation_coverage_status import MetricObservationCoverageStatus
    from .metric_observation_inputs_item import MetricObservationInputsItem
    from .metric_observation_inputs_item_value import MetricObservationInputsItemValue
    from .metric_observation_parameters_value import MetricObservationParametersValue
    from .metric_observation_read_status import MetricObservationReadStatus
    from .metric_observation_status import MetricObservationStatus
    from .not_found_error_body import NotFoundErrorBody
    from .post_alert_payload import PostAlertPayload
    from .post_alert_payload_kind import PostAlertPayloadKind
    from .post_alert_payload_watcher import PostAlertPayloadWatcher
    from .project import Project
    from .run import Run
    from .run_status import RunStatus
    from .service_unavailable_error_body import ServiceUnavailableErrorBody
    from .service_unavailable_error_body_items_item import ServiceUnavailableErrorBodyItemsItem
    from .service_unavailable_error_body_items_item_pairs_item import ServiceUnavailableErrorBodyItemsItemPairsItem
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
    from .service_unavailable_error_body_items_item_status import ServiceUnavailableErrorBodyItemsItemStatus
    from .stock_pairing import StockPairing
    from .stock_pairing_stock_verdict import StockPairingStockVerdict
    from .token_market import TokenMarket
    from .token_market_alternatives_item import TokenMarketAlternativesItem
    from .token_market_burned_raw import TokenMarketBurnedRaw
    from .token_market_decimals import TokenMarketDecimals
    from .token_market_holders import TokenMarketHolders
    from .token_market_market_cap_usd import TokenMarketMarketCapUsd
    from .token_market_price_usd import TokenMarketPriceUsd
    from .token_market_robinhood_app import TokenMarketRobinhoodApp
    from .token_market_robinhood_app_match import TokenMarketRobinhoodAppMatch
    from .token_market_robinhood_app_pairs_item import TokenMarketRobinhoodAppPairsItem
    from .token_market_robinhood_app_pairs_item_asset_currency import TokenMarketRobinhoodAppPairsItemAssetCurrency
    from .token_market_robinhood_app_pairs_item_quote_currency import TokenMarketRobinhoodAppPairsItemQuoteCurrency
    from .token_market_robinhood_app_pairs_item_tradability import TokenMarketRobinhoodAppPairsItemTradability
    from .token_market_robinhood_app_pairs_item_tradability_by_account_type_value import (
        TokenMarketRobinhoodAppPairsItemTradabilityByAccountTypeValue,
    )
    from .token_market_robinhood_app_status import TokenMarketRobinhoodAppStatus
    from .token_market_selection import TokenMarketSelection
    from .token_market_selection_status import TokenMarketSelectionStatus
    from .token_market_stock_pairings_item import TokenMarketStockPairingsItem
    from .token_market_stock_pairings_item_stock_verdict import TokenMarketStockPairingsItemStockVerdict
    from .token_market_swaps24h import TokenMarketSwaps24H
    from .token_market_total_supply_raw import TokenMarketTotalSupplyRaw
    from .token_market_transactions24h import TokenMarketTransactions24H
    from .token_market_trust import TokenMarketTrust
    from .token_market_v3quote_holdings_usd import TokenMarketV3QuoteHoldingsUsd
    from .token_market_v4one_percent_depth_usd import TokenMarketV4OnePercentDepthUsd
    from .token_market_volume_scope import TokenMarketVolumeScope
    from .token_market_volume_usd24h import TokenMarketVolumeUsd24H
    from .too_many_requests_error_body import TooManyRequestsErrorBody
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .watcher import Watcher
    from .watcher_delivery import WatcherDelivery
    from .watcher_kind import WatcherKind
    from .watcher_last_delivery import WatcherLastDelivery
    from .watcher_status import WatcherStatus
    from .webhook import Webhook
    from .webhook_created import WebhookCreated
    from .webhook_delivery import WebhookDelivery
    from .webhook_delivery_kind import WebhookDeliveryKind
    from .webhook_delivery_watcher import WebhookDeliveryWatcher
_dynamic_imports: typing.Dict[str, str] = {
    "AppCatalogPage": ".app_catalog_page",
    "AppCatalogPageItemsItem": ".app_catalog_page_items_item",
    "AppCatalogPageItemsItemPairsItem": ".app_catalog_page_items_item_pairs_item",
    "AppCatalogPageItemsItemPairsItemAssetCurrency": ".app_catalog_page_items_item_pairs_item_asset_currency",
    "AppCatalogPageItemsItemPairsItemQuoteCurrency": ".app_catalog_page_items_item_pairs_item_quote_currency",
    "AppCatalogPageItemsItemPairsItemTradability": ".app_catalog_page_items_item_pairs_item_tradability",
    "AppCatalogPageItemsItemPairsItemTradabilityByAccountTypeValue": ".app_catalog_page_items_item_pairs_item_tradability_by_account_type_value",
    "AppCatalogPageItemsItemStatus": ".app_catalog_page_items_item_status",
    "AppCatalogStatus": ".app_catalog_status",
    "AppCatalogStatusMatch": ".app_catalog_status_match",
    "AppCatalogStatusPairsItem": ".app_catalog_status_pairs_item",
    "AppCatalogStatusPairsItemAssetCurrency": ".app_catalog_status_pairs_item_asset_currency",
    "AppCatalogStatusPairsItemQuoteCurrency": ".app_catalog_status_pairs_item_quote_currency",
    "AppCatalogStatusPairsItemTradability": ".app_catalog_status_pairs_item_tradability",
    "AppCatalogStatusPairsItemTradabilityByAccountTypeValue": ".app_catalog_status_pairs_item_tradability_by_account_type_value",
    "AppCatalogStatusStatus": ".app_catalog_status_status",
    "Asset": ".asset",
    "AssetAssetType": ".asset_asset_type",
    "AuthorityEvent": ".authority_event",
    "BadRequestErrorBody": ".bad_request_error_body",
    "Chain": ".chain",
    "ChainNetwork": ".chain_network",
    "Error": ".error",
    "ForbiddenErrorBody": ".forbidden_error_body",
    "MarketSelection": ".market_selection",
    "MarketSelectionStatus": ".market_selection_status",
    "MetricObservation": ".metric_observation",
    "MetricObservationCoverage": ".metric_observation_coverage",
    "MetricObservationCoverageStatus": ".metric_observation_coverage_status",
    "MetricObservationInputsItem": ".metric_observation_inputs_item",
    "MetricObservationInputsItemValue": ".metric_observation_inputs_item_value",
    "MetricObservationParametersValue": ".metric_observation_parameters_value",
    "MetricObservationReadStatus": ".metric_observation_read_status",
    "MetricObservationStatus": ".metric_observation_status",
    "NotFoundErrorBody": ".not_found_error_body",
    "PostAlertPayload": ".post_alert_payload",
    "PostAlertPayloadKind": ".post_alert_payload_kind",
    "PostAlertPayloadWatcher": ".post_alert_payload_watcher",
    "Project": ".project",
    "Run": ".run",
    "RunStatus": ".run_status",
    "ServiceUnavailableErrorBody": ".service_unavailable_error_body",
    "ServiceUnavailableErrorBodyItemsItem": ".service_unavailable_error_body_items_item",
    "ServiceUnavailableErrorBodyItemsItemPairsItem": ".service_unavailable_error_body_items_item_pairs_item",
    "ServiceUnavailableErrorBodyItemsItemPairsItemAssetCurrency": ".service_unavailable_error_body_items_item_pairs_item_asset_currency",
    "ServiceUnavailableErrorBodyItemsItemPairsItemQuoteCurrency": ".service_unavailable_error_body_items_item_pairs_item_quote_currency",
    "ServiceUnavailableErrorBodyItemsItemPairsItemTradability": ".service_unavailable_error_body_items_item_pairs_item_tradability",
    "ServiceUnavailableErrorBodyItemsItemPairsItemTradabilityByAccountTypeValue": ".service_unavailable_error_body_items_item_pairs_item_tradability_by_account_type_value",
    "ServiceUnavailableErrorBodyItemsItemStatus": ".service_unavailable_error_body_items_item_status",
    "StockPairing": ".stock_pairing",
    "StockPairingStockVerdict": ".stock_pairing_stock_verdict",
    "TokenMarket": ".token_market",
    "TokenMarketAlternativesItem": ".token_market_alternatives_item",
    "TokenMarketBurnedRaw": ".token_market_burned_raw",
    "TokenMarketDecimals": ".token_market_decimals",
    "TokenMarketHolders": ".token_market_holders",
    "TokenMarketMarketCapUsd": ".token_market_market_cap_usd",
    "TokenMarketPriceUsd": ".token_market_price_usd",
    "TokenMarketRobinhoodApp": ".token_market_robinhood_app",
    "TokenMarketRobinhoodAppMatch": ".token_market_robinhood_app_match",
    "TokenMarketRobinhoodAppPairsItem": ".token_market_robinhood_app_pairs_item",
    "TokenMarketRobinhoodAppPairsItemAssetCurrency": ".token_market_robinhood_app_pairs_item_asset_currency",
    "TokenMarketRobinhoodAppPairsItemQuoteCurrency": ".token_market_robinhood_app_pairs_item_quote_currency",
    "TokenMarketRobinhoodAppPairsItemTradability": ".token_market_robinhood_app_pairs_item_tradability",
    "TokenMarketRobinhoodAppPairsItemTradabilityByAccountTypeValue": ".token_market_robinhood_app_pairs_item_tradability_by_account_type_value",
    "TokenMarketRobinhoodAppStatus": ".token_market_robinhood_app_status",
    "TokenMarketSelection": ".token_market_selection",
    "TokenMarketSelectionStatus": ".token_market_selection_status",
    "TokenMarketStockPairingsItem": ".token_market_stock_pairings_item",
    "TokenMarketStockPairingsItemStockVerdict": ".token_market_stock_pairings_item_stock_verdict",
    "TokenMarketSwaps24H": ".token_market_swaps24h",
    "TokenMarketTotalSupplyRaw": ".token_market_total_supply_raw",
    "TokenMarketTransactions24H": ".token_market_transactions24h",
    "TokenMarketTrust": ".token_market_trust",
    "TokenMarketV3QuoteHoldingsUsd": ".token_market_v3quote_holdings_usd",
    "TokenMarketV4OnePercentDepthUsd": ".token_market_v4one_percent_depth_usd",
    "TokenMarketVolumeScope": ".token_market_volume_scope",
    "TokenMarketVolumeUsd24H": ".token_market_volume_usd24h",
    "TooManyRequestsErrorBody": ".too_many_requests_error_body",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "Watcher": ".watcher",
    "WatcherDelivery": ".watcher_delivery",
    "WatcherKind": ".watcher_kind",
    "WatcherLastDelivery": ".watcher_last_delivery",
    "WatcherStatus": ".watcher_status",
    "Webhook": ".webhook",
    "WebhookCreated": ".webhook_created",
    "WebhookDelivery": ".webhook_delivery",
    "WebhookDeliveryKind": ".webhook_delivery_kind",
    "WebhookDeliveryWatcher": ".webhook_delivery_watcher",
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
    "AppCatalogPage",
    "AppCatalogPageItemsItem",
    "AppCatalogPageItemsItemPairsItem",
    "AppCatalogPageItemsItemPairsItemAssetCurrency",
    "AppCatalogPageItemsItemPairsItemQuoteCurrency",
    "AppCatalogPageItemsItemPairsItemTradability",
    "AppCatalogPageItemsItemPairsItemTradabilityByAccountTypeValue",
    "AppCatalogPageItemsItemStatus",
    "AppCatalogStatus",
    "AppCatalogStatusMatch",
    "AppCatalogStatusPairsItem",
    "AppCatalogStatusPairsItemAssetCurrency",
    "AppCatalogStatusPairsItemQuoteCurrency",
    "AppCatalogStatusPairsItemTradability",
    "AppCatalogStatusPairsItemTradabilityByAccountTypeValue",
    "AppCatalogStatusStatus",
    "Asset",
    "AssetAssetType",
    "AuthorityEvent",
    "BadRequestErrorBody",
    "Chain",
    "ChainNetwork",
    "Error",
    "ForbiddenErrorBody",
    "MarketSelection",
    "MarketSelectionStatus",
    "MetricObservation",
    "MetricObservationCoverage",
    "MetricObservationCoverageStatus",
    "MetricObservationInputsItem",
    "MetricObservationInputsItemValue",
    "MetricObservationParametersValue",
    "MetricObservationReadStatus",
    "MetricObservationStatus",
    "NotFoundErrorBody",
    "PostAlertPayload",
    "PostAlertPayloadKind",
    "PostAlertPayloadWatcher",
    "Project",
    "Run",
    "RunStatus",
    "ServiceUnavailableErrorBody",
    "ServiceUnavailableErrorBodyItemsItem",
    "ServiceUnavailableErrorBodyItemsItemPairsItem",
    "ServiceUnavailableErrorBodyItemsItemPairsItemAssetCurrency",
    "ServiceUnavailableErrorBodyItemsItemPairsItemQuoteCurrency",
    "ServiceUnavailableErrorBodyItemsItemPairsItemTradability",
    "ServiceUnavailableErrorBodyItemsItemPairsItemTradabilityByAccountTypeValue",
    "ServiceUnavailableErrorBodyItemsItemStatus",
    "StockPairing",
    "StockPairingStockVerdict",
    "TokenMarket",
    "TokenMarketAlternativesItem",
    "TokenMarketBurnedRaw",
    "TokenMarketDecimals",
    "TokenMarketHolders",
    "TokenMarketMarketCapUsd",
    "TokenMarketPriceUsd",
    "TokenMarketRobinhoodApp",
    "TokenMarketRobinhoodAppMatch",
    "TokenMarketRobinhoodAppPairsItem",
    "TokenMarketRobinhoodAppPairsItemAssetCurrency",
    "TokenMarketRobinhoodAppPairsItemQuoteCurrency",
    "TokenMarketRobinhoodAppPairsItemTradability",
    "TokenMarketRobinhoodAppPairsItemTradabilityByAccountTypeValue",
    "TokenMarketRobinhoodAppStatus",
    "TokenMarketSelection",
    "TokenMarketSelectionStatus",
    "TokenMarketStockPairingsItem",
    "TokenMarketStockPairingsItemStockVerdict",
    "TokenMarketSwaps24H",
    "TokenMarketTotalSupplyRaw",
    "TokenMarketTransactions24H",
    "TokenMarketTrust",
    "TokenMarketV3QuoteHoldingsUsd",
    "TokenMarketV4OnePercentDepthUsd",
    "TokenMarketVolumeScope",
    "TokenMarketVolumeUsd24H",
    "TooManyRequestsErrorBody",
    "UnauthorizedErrorBody",
    "Watcher",
    "WatcherDelivery",
    "WatcherKind",
    "WatcherLastDelivery",
    "WatcherStatus",
    "Webhook",
    "WebhookCreated",
    "WebhookDelivery",
    "WebhookDeliveryKind",
    "WebhookDeliveryWatcher",
]
