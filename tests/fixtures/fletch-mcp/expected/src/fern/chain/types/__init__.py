



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_chains_chain_id_bridge_response import GetChainsChainIdBridgeResponse
    from .get_chains_chain_id_control_plane_response import GetChainsChainIdControlPlaneResponse
    from .get_chains_chain_id_corporate_actions_response import GetChainsChainIdCorporateActionsResponse
    from .get_chains_chain_id_dex_response import GetChainsChainIdDexResponse
    from .get_chains_chain_id_dex_response_discovery_item import GetChainsChainIdDexResponseDiscoveryItem
    from .get_chains_chain_id_dex_response_venues_item import GetChainsChainIdDexResponseVenuesItem
    from .get_chains_chain_id_dex_response_venues_item_venue import GetChainsChainIdDexResponseVenuesItemVenue
    from .get_chains_chain_id_health_response import GetChainsChainIdHealthResponse
    from .get_chains_chain_id_issuer_request_kind import GetChainsChainIdIssuerRequestKind
    from .get_chains_chain_id_issuer_response import GetChainsChainIdIssuerResponse
    from .get_chains_chain_id_lookalikes_response import GetChainsChainIdLookalikesResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetChainsChainIdBridgeResponse": ".get_chains_chain_id_bridge_response",
    "GetChainsChainIdControlPlaneResponse": ".get_chains_chain_id_control_plane_response",
    "GetChainsChainIdCorporateActionsResponse": ".get_chains_chain_id_corporate_actions_response",
    "GetChainsChainIdDexResponse": ".get_chains_chain_id_dex_response",
    "GetChainsChainIdDexResponseDiscoveryItem": ".get_chains_chain_id_dex_response_discovery_item",
    "GetChainsChainIdDexResponseVenuesItem": ".get_chains_chain_id_dex_response_venues_item",
    "GetChainsChainIdDexResponseVenuesItemVenue": ".get_chains_chain_id_dex_response_venues_item_venue",
    "GetChainsChainIdHealthResponse": ".get_chains_chain_id_health_response",
    "GetChainsChainIdIssuerRequestKind": ".get_chains_chain_id_issuer_request_kind",
    "GetChainsChainIdIssuerResponse": ".get_chains_chain_id_issuer_response",
    "GetChainsChainIdLookalikesResponse": ".get_chains_chain_id_lookalikes_response",
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
    "GetChainsChainIdBridgeResponse",
    "GetChainsChainIdControlPlaneResponse",
    "GetChainsChainIdCorporateActionsResponse",
    "GetChainsChainIdDexResponse",
    "GetChainsChainIdDexResponseDiscoveryItem",
    "GetChainsChainIdDexResponseVenuesItem",
    "GetChainsChainIdDexResponseVenuesItemVenue",
    "GetChainsChainIdHealthResponse",
    "GetChainsChainIdIssuerRequestKind",
    "GetChainsChainIdIssuerResponse",
    "GetChainsChainIdLookalikesResponse",
]
