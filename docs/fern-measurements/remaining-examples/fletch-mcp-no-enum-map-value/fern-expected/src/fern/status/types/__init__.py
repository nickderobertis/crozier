



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_chains_chain_id_status_response import GetChainsChainIdStatusResponse
    from .get_chains_chain_id_status_response_jobs_item import GetChainsChainIdStatusResponseJobsItem
    from .get_chains_chain_id_status_response_jobs_item_metadata_backlog import (
        GetChainsChainIdStatusResponseJobsItemMetadataBacklog,
    )
    from .get_chains_chain_id_status_response_jobs_item_metric_coverage_value import (
        GetChainsChainIdStatusResponseJobsItemMetricCoverageValue,
    )
    from .get_chains_chain_id_status_response_jobs_item_verdict import GetChainsChainIdStatusResponseJobsItemVerdict
    from .get_chains_chain_id_status_response_scouting import GetChainsChainIdStatusResponseScouting
    from .get_chains_chain_id_status_response_scouting_explorer import GetChainsChainIdStatusResponseScoutingExplorer
    from .get_chains_chain_id_status_response_scouting_explorer_provider import (
        GetChainsChainIdStatusResponseScoutingExplorerProvider,
    )
    from .get_chains_chain_id_status_response_swap_indexer import GetChainsChainIdStatusResponseSwapIndexer
    from .get_chains_chain_id_status_response_swap_indexer_coverage_scope import (
        GetChainsChainIdStatusResponseSwapIndexerCoverageScope,
    )
    from .get_chains_chain_id_status_response_swap_indexer_mode import GetChainsChainIdStatusResponseSwapIndexerMode
    from .get_chains_chain_id_status_response_swap_indexer_tiers_item import (
        GetChainsChainIdStatusResponseSwapIndexerTiersItem,
    )
    from .get_chains_chain_id_status_response_swap_indexer_tiers_item_tier import (
        GetChainsChainIdStatusResponseSwapIndexerTiersItemTier,
    )
    from .get_chains_chain_id_status_response_swap_indexer_tiers_scope import (
        GetChainsChainIdStatusResponseSwapIndexerTiersScope,
    )
    from .get_chains_chain_id_status_response_swap_indexer_valuation_methods_item import (
        GetChainsChainIdStatusResponseSwapIndexerValuationMethodsItem,
    )
    from .get_chains_chain_id_status_response_verdict import GetChainsChainIdStatusResponseVerdict
    from .get_status_response import GetStatusResponse
    from .get_status_response_jobs_item import GetStatusResponseJobsItem
    from .get_status_response_jobs_item_metadata_backlog import GetStatusResponseJobsItemMetadataBacklog
    from .get_status_response_jobs_item_metric_coverage_value import GetStatusResponseJobsItemMetricCoverageValue
    from .get_status_response_jobs_item_verdict import GetStatusResponseJobsItemVerdict
    from .get_status_response_scouting import GetStatusResponseScouting
    from .get_status_response_scouting_explorer import GetStatusResponseScoutingExplorer
    from .get_status_response_scouting_explorer_provider import GetStatusResponseScoutingExplorerProvider
    from .get_status_response_swap_indexer import GetStatusResponseSwapIndexer
    from .get_status_response_swap_indexer_coverage_scope import GetStatusResponseSwapIndexerCoverageScope
    from .get_status_response_swap_indexer_mode import GetStatusResponseSwapIndexerMode
    from .get_status_response_swap_indexer_tiers_item import GetStatusResponseSwapIndexerTiersItem
    from .get_status_response_swap_indexer_tiers_item_tier import GetStatusResponseSwapIndexerTiersItemTier
    from .get_status_response_swap_indexer_tiers_scope import GetStatusResponseSwapIndexerTiersScope
    from .get_status_response_swap_indexer_valuation_methods_item import (
        GetStatusResponseSwapIndexerValuationMethodsItem,
    )
    from .get_status_response_verdict import GetStatusResponseVerdict
_dynamic_imports: typing.Dict[str, str] = {
    "GetChainsChainIdStatusResponse": ".get_chains_chain_id_status_response",
    "GetChainsChainIdStatusResponseJobsItem": ".get_chains_chain_id_status_response_jobs_item",
    "GetChainsChainIdStatusResponseJobsItemMetadataBacklog": ".get_chains_chain_id_status_response_jobs_item_metadata_backlog",
    "GetChainsChainIdStatusResponseJobsItemMetricCoverageValue": ".get_chains_chain_id_status_response_jobs_item_metric_coverage_value",
    "GetChainsChainIdStatusResponseJobsItemVerdict": ".get_chains_chain_id_status_response_jobs_item_verdict",
    "GetChainsChainIdStatusResponseScouting": ".get_chains_chain_id_status_response_scouting",
    "GetChainsChainIdStatusResponseScoutingExplorer": ".get_chains_chain_id_status_response_scouting_explorer",
    "GetChainsChainIdStatusResponseScoutingExplorerProvider": ".get_chains_chain_id_status_response_scouting_explorer_provider",
    "GetChainsChainIdStatusResponseSwapIndexer": ".get_chains_chain_id_status_response_swap_indexer",
    "GetChainsChainIdStatusResponseSwapIndexerCoverageScope": ".get_chains_chain_id_status_response_swap_indexer_coverage_scope",
    "GetChainsChainIdStatusResponseSwapIndexerMode": ".get_chains_chain_id_status_response_swap_indexer_mode",
    "GetChainsChainIdStatusResponseSwapIndexerTiersItem": ".get_chains_chain_id_status_response_swap_indexer_tiers_item",
    "GetChainsChainIdStatusResponseSwapIndexerTiersItemTier": ".get_chains_chain_id_status_response_swap_indexer_tiers_item_tier",
    "GetChainsChainIdStatusResponseSwapIndexerTiersScope": ".get_chains_chain_id_status_response_swap_indexer_tiers_scope",
    "GetChainsChainIdStatusResponseSwapIndexerValuationMethodsItem": ".get_chains_chain_id_status_response_swap_indexer_valuation_methods_item",
    "GetChainsChainIdStatusResponseVerdict": ".get_chains_chain_id_status_response_verdict",
    "GetStatusResponse": ".get_status_response",
    "GetStatusResponseJobsItem": ".get_status_response_jobs_item",
    "GetStatusResponseJobsItemMetadataBacklog": ".get_status_response_jobs_item_metadata_backlog",
    "GetStatusResponseJobsItemMetricCoverageValue": ".get_status_response_jobs_item_metric_coverage_value",
    "GetStatusResponseJobsItemVerdict": ".get_status_response_jobs_item_verdict",
    "GetStatusResponseScouting": ".get_status_response_scouting",
    "GetStatusResponseScoutingExplorer": ".get_status_response_scouting_explorer",
    "GetStatusResponseScoutingExplorerProvider": ".get_status_response_scouting_explorer_provider",
    "GetStatusResponseSwapIndexer": ".get_status_response_swap_indexer",
    "GetStatusResponseSwapIndexerCoverageScope": ".get_status_response_swap_indexer_coverage_scope",
    "GetStatusResponseSwapIndexerMode": ".get_status_response_swap_indexer_mode",
    "GetStatusResponseSwapIndexerTiersItem": ".get_status_response_swap_indexer_tiers_item",
    "GetStatusResponseSwapIndexerTiersItemTier": ".get_status_response_swap_indexer_tiers_item_tier",
    "GetStatusResponseSwapIndexerTiersScope": ".get_status_response_swap_indexer_tiers_scope",
    "GetStatusResponseSwapIndexerValuationMethodsItem": ".get_status_response_swap_indexer_valuation_methods_item",
    "GetStatusResponseVerdict": ".get_status_response_verdict",
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
