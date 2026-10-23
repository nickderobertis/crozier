



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_chains_chain_id_assets_request_trust import GetChainsChainIdAssetsRequestTrust
    from .get_chains_chain_id_assets_response import GetChainsChainIdAssetsResponse
    from .get_chains_chain_id_assets_response_assets_item import GetChainsChainIdAssetsResponseAssetsItem
    from .get_chains_chain_id_assets_response_assets_item_asset_type import (
        GetChainsChainIdAssetsResponseAssetsItemAssetType,
    )
    from .get_chains_chain_id_assets_response_assets_item_state import GetChainsChainIdAssetsResponseAssetsItemState
    from .get_chains_chain_id_assets_response_assets_item_state_feed import (
        GetChainsChainIdAssetsResponseAssetsItemStateFeed,
    )
    from .get_chains_chain_id_assets_response_assets_item_state_quote import (
        GetChainsChainIdAssetsResponseAssetsItemStateQuote,
    )
    from .get_chains_chain_id_assets_response_assets_item_trust import GetChainsChainIdAssetsResponseAssetsItemTrust
    from .get_chains_chain_id_assets_response_assets_item_trust_level import (
        GetChainsChainIdAssetsResponseAssetsItemTrustLevel,
    )
    from .get_chains_chain_id_assets_symbol_activity_response import GetChainsChainIdAssetsSymbolActivityResponse
    from .get_chains_chain_id_assets_symbol_feed_rounds_response import GetChainsChainIdAssetsSymbolFeedRoundsResponse
    from .get_chains_chain_id_assets_symbol_history_response import GetChainsChainIdAssetsSymbolHistoryResponse
    from .get_chains_chain_id_assets_symbol_history_response_coverage import (
        GetChainsChainIdAssetsSymbolHistoryResponseCoverage,
    )
    from .get_chains_chain_id_assets_symbol_holders_response import GetChainsChainIdAssetsSymbolHoldersResponse
    from .get_chains_chain_id_assets_symbol_holders_response_holders_item import (
        GetChainsChainIdAssetsSymbolHoldersResponseHoldersItem,
    )
    from .get_chains_chain_id_assets_symbol_holders_response_holders_item_label_kind import (
        GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind,
    )
    from .get_chains_chain_id_assets_symbol_holders_response_holders_item_sits import (
        GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits,
    )
    from .get_chains_chain_id_assets_symbol_pools_response import GetChainsChainIdAssetsSymbolPoolsResponse
    from .get_chains_chain_id_assets_symbol_pools_response_discovery_item import (
        GetChainsChainIdAssetsSymbolPoolsResponseDiscoveryItem,
    )
    from .get_chains_chain_id_assets_symbol_response import GetChainsChainIdAssetsSymbolResponse
    from .get_chains_chain_id_assets_symbol_response_asset import GetChainsChainIdAssetsSymbolResponseAsset
    from .get_chains_chain_id_assets_symbol_response_asset_asset_type import (
        GetChainsChainIdAssetsSymbolResponseAssetAssetType,
    )
    from .get_chains_chain_id_assets_symbol_response_state import GetChainsChainIdAssetsSymbolResponseState
    from .get_chains_chain_id_assets_symbol_response_state_feed import GetChainsChainIdAssetsSymbolResponseStateFeed
    from .get_chains_chain_id_assets_symbol_response_state_quote import GetChainsChainIdAssetsSymbolResponseStateQuote
    from .get_chains_chain_id_assets_symbol_response_trust import GetChainsChainIdAssetsSymbolResponseTrust
    from .get_chains_chain_id_assets_symbol_response_trust_level import GetChainsChainIdAssetsSymbolResponseTrustLevel
_dynamic_imports: typing.Dict[str, str] = {
    "GetChainsChainIdAssetsRequestTrust": ".get_chains_chain_id_assets_request_trust",
    "GetChainsChainIdAssetsResponse": ".get_chains_chain_id_assets_response",
    "GetChainsChainIdAssetsResponseAssetsItem": ".get_chains_chain_id_assets_response_assets_item",
    "GetChainsChainIdAssetsResponseAssetsItemAssetType": ".get_chains_chain_id_assets_response_assets_item_asset_type",
    "GetChainsChainIdAssetsResponseAssetsItemState": ".get_chains_chain_id_assets_response_assets_item_state",
    "GetChainsChainIdAssetsResponseAssetsItemStateFeed": ".get_chains_chain_id_assets_response_assets_item_state_feed",
    "GetChainsChainIdAssetsResponseAssetsItemStateQuote": ".get_chains_chain_id_assets_response_assets_item_state_quote",
    "GetChainsChainIdAssetsResponseAssetsItemTrust": ".get_chains_chain_id_assets_response_assets_item_trust",
    "GetChainsChainIdAssetsResponseAssetsItemTrustLevel": ".get_chains_chain_id_assets_response_assets_item_trust_level",
    "GetChainsChainIdAssetsSymbolActivityResponse": ".get_chains_chain_id_assets_symbol_activity_response",
    "GetChainsChainIdAssetsSymbolFeedRoundsResponse": ".get_chains_chain_id_assets_symbol_feed_rounds_response",
    "GetChainsChainIdAssetsSymbolHistoryResponse": ".get_chains_chain_id_assets_symbol_history_response",
    "GetChainsChainIdAssetsSymbolHistoryResponseCoverage": ".get_chains_chain_id_assets_symbol_history_response_coverage",
    "GetChainsChainIdAssetsSymbolHoldersResponse": ".get_chains_chain_id_assets_symbol_holders_response",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItem": ".get_chains_chain_id_assets_symbol_holders_response_holders_item",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind": ".get_chains_chain_id_assets_symbol_holders_response_holders_item_label_kind",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits": ".get_chains_chain_id_assets_symbol_holders_response_holders_item_sits",
    "GetChainsChainIdAssetsSymbolPoolsResponse": ".get_chains_chain_id_assets_symbol_pools_response",
    "GetChainsChainIdAssetsSymbolPoolsResponseDiscoveryItem": ".get_chains_chain_id_assets_symbol_pools_response_discovery_item",
    "GetChainsChainIdAssetsSymbolResponse": ".get_chains_chain_id_assets_symbol_response",
    "GetChainsChainIdAssetsSymbolResponseAsset": ".get_chains_chain_id_assets_symbol_response_asset",
    "GetChainsChainIdAssetsSymbolResponseAssetAssetType": ".get_chains_chain_id_assets_symbol_response_asset_asset_type",
    "GetChainsChainIdAssetsSymbolResponseState": ".get_chains_chain_id_assets_symbol_response_state",
    "GetChainsChainIdAssetsSymbolResponseStateFeed": ".get_chains_chain_id_assets_symbol_response_state_feed",
    "GetChainsChainIdAssetsSymbolResponseStateQuote": ".get_chains_chain_id_assets_symbol_response_state_quote",
    "GetChainsChainIdAssetsSymbolResponseTrust": ".get_chains_chain_id_assets_symbol_response_trust",
    "GetChainsChainIdAssetsSymbolResponseTrustLevel": ".get_chains_chain_id_assets_symbol_response_trust_level",
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
    "GetChainsChainIdAssetsRequestTrust",
    "GetChainsChainIdAssetsResponse",
    "GetChainsChainIdAssetsResponseAssetsItem",
    "GetChainsChainIdAssetsResponseAssetsItemAssetType",
    "GetChainsChainIdAssetsResponseAssetsItemState",
    "GetChainsChainIdAssetsResponseAssetsItemStateFeed",
    "GetChainsChainIdAssetsResponseAssetsItemStateQuote",
    "GetChainsChainIdAssetsResponseAssetsItemTrust",
    "GetChainsChainIdAssetsResponseAssetsItemTrustLevel",
    "GetChainsChainIdAssetsSymbolActivityResponse",
    "GetChainsChainIdAssetsSymbolFeedRoundsResponse",
    "GetChainsChainIdAssetsSymbolHistoryResponse",
    "GetChainsChainIdAssetsSymbolHistoryResponseCoverage",
    "GetChainsChainIdAssetsSymbolHoldersResponse",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItem",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits",
    "GetChainsChainIdAssetsSymbolPoolsResponse",
    "GetChainsChainIdAssetsSymbolPoolsResponseDiscoveryItem",
    "GetChainsChainIdAssetsSymbolResponse",
    "GetChainsChainIdAssetsSymbolResponseAsset",
    "GetChainsChainIdAssetsSymbolResponseAssetAssetType",
    "GetChainsChainIdAssetsSymbolResponseState",
    "GetChainsChainIdAssetsSymbolResponseStateFeed",
    "GetChainsChainIdAssetsSymbolResponseStateQuote",
    "GetChainsChainIdAssetsSymbolResponseTrust",
    "GetChainsChainIdAssetsSymbolResponseTrustLevel",
]
