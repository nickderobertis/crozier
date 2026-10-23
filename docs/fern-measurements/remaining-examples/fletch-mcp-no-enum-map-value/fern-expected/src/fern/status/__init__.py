



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetChainsChainIdStatusResponse,
        GetChainsChainIdStatusResponseJobsItem,
        GetChainsChainIdStatusResponseJobsItemMetadataBacklog,
        GetChainsChainIdStatusResponseJobsItemMetricCoverageValue,
        GetChainsChainIdStatusResponseJobsItemVerdict,
        GetChainsChainIdStatusResponseScouting,
        GetChainsChainIdStatusResponseScoutingExplorer,
        GetChainsChainIdStatusResponseScoutingExplorerProvider,
        GetChainsChainIdStatusResponseSwapIndexer,
        GetChainsChainIdStatusResponseSwapIndexerCoverageScope,
        GetChainsChainIdStatusResponseSwapIndexerMode,
        GetChainsChainIdStatusResponseSwapIndexerTiersItem,
        GetChainsChainIdStatusResponseSwapIndexerTiersItemTier,
        GetChainsChainIdStatusResponseSwapIndexerTiersScope,
        GetChainsChainIdStatusResponseSwapIndexerValuationMethodsItem,
        GetChainsChainIdStatusResponseVerdict,
        GetStatusResponse,
        GetStatusResponseJobsItem,
        GetStatusResponseJobsItemMetadataBacklog,
        GetStatusResponseJobsItemMetricCoverageValue,
        GetStatusResponseJobsItemVerdict,
        GetStatusResponseScouting,
        GetStatusResponseScoutingExplorer,
        GetStatusResponseScoutingExplorerProvider,
        GetStatusResponseSwapIndexer,
        GetStatusResponseSwapIndexerCoverageScope,
        GetStatusResponseSwapIndexerMode,
        GetStatusResponseSwapIndexerTiersItem,
        GetStatusResponseSwapIndexerTiersItemTier,
        GetStatusResponseSwapIndexerTiersScope,
        GetStatusResponseSwapIndexerValuationMethodsItem,
        GetStatusResponseVerdict,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetChainsChainIdStatusResponse": ".types",
    "GetChainsChainIdStatusResponseJobsItem": ".types",
    "GetChainsChainIdStatusResponseJobsItemMetadataBacklog": ".types",
    "GetChainsChainIdStatusResponseJobsItemMetricCoverageValue": ".types",
    "GetChainsChainIdStatusResponseJobsItemVerdict": ".types",
    "GetChainsChainIdStatusResponseScouting": ".types",
    "GetChainsChainIdStatusResponseScoutingExplorer": ".types",
    "GetChainsChainIdStatusResponseScoutingExplorerProvider": ".types",
    "GetChainsChainIdStatusResponseSwapIndexer": ".types",
    "GetChainsChainIdStatusResponseSwapIndexerCoverageScope": ".types",
    "GetChainsChainIdStatusResponseSwapIndexerMode": ".types",
    "GetChainsChainIdStatusResponseSwapIndexerTiersItem": ".types",
    "GetChainsChainIdStatusResponseSwapIndexerTiersItemTier": ".types",
    "GetChainsChainIdStatusResponseSwapIndexerTiersScope": ".types",
    "GetChainsChainIdStatusResponseSwapIndexerValuationMethodsItem": ".types",
    "GetChainsChainIdStatusResponseVerdict": ".types",
    "GetStatusResponse": ".types",
    "GetStatusResponseJobsItem": ".types",
    "GetStatusResponseJobsItemMetadataBacklog": ".types",
    "GetStatusResponseJobsItemMetricCoverageValue": ".types",
    "GetStatusResponseJobsItemVerdict": ".types",
    "GetStatusResponseScouting": ".types",
    "GetStatusResponseScoutingExplorer": ".types",
    "GetStatusResponseScoutingExplorerProvider": ".types",
    "GetStatusResponseSwapIndexer": ".types",
    "GetStatusResponseSwapIndexerCoverageScope": ".types",
    "GetStatusResponseSwapIndexerMode": ".types",
    "GetStatusResponseSwapIndexerTiersItem": ".types",
    "GetStatusResponseSwapIndexerTiersItemTier": ".types",
    "GetStatusResponseSwapIndexerTiersScope": ".types",
    "GetStatusResponseSwapIndexerValuationMethodsItem": ".types",
    "GetStatusResponseVerdict": ".types",
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
    "GetChainsChainIdStatusResponse",
    "GetChainsChainIdStatusResponseJobsItem",
    "GetChainsChainIdStatusResponseJobsItemMetadataBacklog",
    "GetChainsChainIdStatusResponseJobsItemMetricCoverageValue",
    "GetChainsChainIdStatusResponseJobsItemVerdict",
    "GetChainsChainIdStatusResponseScouting",
    "GetChainsChainIdStatusResponseScoutingExplorer",
    "GetChainsChainIdStatusResponseScoutingExplorerProvider",
    "GetChainsChainIdStatusResponseSwapIndexer",
    "GetChainsChainIdStatusResponseSwapIndexerCoverageScope",
    "GetChainsChainIdStatusResponseSwapIndexerMode",
    "GetChainsChainIdStatusResponseSwapIndexerTiersItem",
    "GetChainsChainIdStatusResponseSwapIndexerTiersItemTier",
    "GetChainsChainIdStatusResponseSwapIndexerTiersScope",
    "GetChainsChainIdStatusResponseSwapIndexerValuationMethodsItem",
    "GetChainsChainIdStatusResponseVerdict",
    "GetStatusResponse",
    "GetStatusResponseJobsItem",
    "GetStatusResponseJobsItemMetadataBacklog",
    "GetStatusResponseJobsItemMetricCoverageValue",
    "GetStatusResponseJobsItemVerdict",
    "GetStatusResponseScouting",
    "GetStatusResponseScoutingExplorer",
    "GetStatusResponseScoutingExplorerProvider",
    "GetStatusResponseSwapIndexer",
    "GetStatusResponseSwapIndexerCoverageScope",
    "GetStatusResponseSwapIndexerMode",
    "GetStatusResponseSwapIndexerTiersItem",
    "GetStatusResponseSwapIndexerTiersItemTier",
    "GetStatusResponseSwapIndexerTiersScope",
    "GetStatusResponseSwapIndexerValuationMethodsItem",
    "GetStatusResponseVerdict",
]
