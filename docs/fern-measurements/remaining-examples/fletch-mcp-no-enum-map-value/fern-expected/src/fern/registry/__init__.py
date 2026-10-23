



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetChainsChainIdAssetsRequestTrust,
        GetChainsChainIdAssetsResponse,
        GetChainsChainIdAssetsResponseAssetsItem,
        GetChainsChainIdAssetsResponseAssetsItemAssetType,
        GetChainsChainIdAssetsResponseAssetsItemState,
        GetChainsChainIdAssetsResponseAssetsItemStateFeed,
        GetChainsChainIdAssetsResponseAssetsItemStateQuote,
        GetChainsChainIdAssetsResponseAssetsItemTrust,
        GetChainsChainIdAssetsResponseAssetsItemTrustLevel,
        GetChainsChainIdAssetsSymbolActivityResponse,
        GetChainsChainIdAssetsSymbolFeedRoundsResponse,
        GetChainsChainIdAssetsSymbolHistoryResponse,
        GetChainsChainIdAssetsSymbolHistoryResponseCoverage,
        GetChainsChainIdAssetsSymbolHoldersResponse,
        GetChainsChainIdAssetsSymbolHoldersResponseHoldersItem,
        GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind,
        GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits,
        GetChainsChainIdAssetsSymbolPoolsResponse,
        GetChainsChainIdAssetsSymbolPoolsResponseDiscoveryItem,
        GetChainsChainIdAssetsSymbolResponse,
        GetChainsChainIdAssetsSymbolResponseAsset,
        GetChainsChainIdAssetsSymbolResponseAssetAssetType,
        GetChainsChainIdAssetsSymbolResponseState,
        GetChainsChainIdAssetsSymbolResponseStateFeed,
        GetChainsChainIdAssetsSymbolResponseStateQuote,
        GetChainsChainIdAssetsSymbolResponseTrust,
        GetChainsChainIdAssetsSymbolResponseTrustLevel,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetChainsChainIdAssetsRequestTrust": ".types",
    "GetChainsChainIdAssetsResponse": ".types",
    "GetChainsChainIdAssetsResponseAssetsItem": ".types",
    "GetChainsChainIdAssetsResponseAssetsItemAssetType": ".types",
    "GetChainsChainIdAssetsResponseAssetsItemState": ".types",
    "GetChainsChainIdAssetsResponseAssetsItemStateFeed": ".types",
    "GetChainsChainIdAssetsResponseAssetsItemStateQuote": ".types",
    "GetChainsChainIdAssetsResponseAssetsItemTrust": ".types",
    "GetChainsChainIdAssetsResponseAssetsItemTrustLevel": ".types",
    "GetChainsChainIdAssetsSymbolActivityResponse": ".types",
    "GetChainsChainIdAssetsSymbolFeedRoundsResponse": ".types",
    "GetChainsChainIdAssetsSymbolHistoryResponse": ".types",
    "GetChainsChainIdAssetsSymbolHistoryResponseCoverage": ".types",
    "GetChainsChainIdAssetsSymbolHoldersResponse": ".types",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItem": ".types",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemLabelKind": ".types",
    "GetChainsChainIdAssetsSymbolHoldersResponseHoldersItemSits": ".types",
    "GetChainsChainIdAssetsSymbolPoolsResponse": ".types",
    "GetChainsChainIdAssetsSymbolPoolsResponseDiscoveryItem": ".types",
    "GetChainsChainIdAssetsSymbolResponse": ".types",
    "GetChainsChainIdAssetsSymbolResponseAsset": ".types",
    "GetChainsChainIdAssetsSymbolResponseAssetAssetType": ".types",
    "GetChainsChainIdAssetsSymbolResponseState": ".types",
    "GetChainsChainIdAssetsSymbolResponseStateFeed": ".types",
    "GetChainsChainIdAssetsSymbolResponseStateQuote": ".types",
    "GetChainsChainIdAssetsSymbolResponseTrust": ".types",
    "GetChainsChainIdAssetsSymbolResponseTrustLevel": ".types",
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
