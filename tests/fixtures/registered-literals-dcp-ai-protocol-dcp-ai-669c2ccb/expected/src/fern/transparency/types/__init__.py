



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_gossip_peer_response import AddGossipPeerResponse
    from .add_to_log_response import AddToLogResponse
    from .get_gossip_alerts_response import GetGossipAlertsResponse
    from .get_gossip_peers_response import GetGossipPeersResponse
    from .get_gossip_peers_response_peers_item import GetGossipPeersResponsePeersItem
    from .get_log_root_response import GetLogRootResponse
    from .gossip_exchange_response import GossipExchangeResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AddGossipPeerResponse": ".add_gossip_peer_response",
    "AddToLogResponse": ".add_to_log_response",
    "GetGossipAlertsResponse": ".get_gossip_alerts_response",
    "GetGossipPeersResponse": ".get_gossip_peers_response",
    "GetGossipPeersResponsePeersItem": ".get_gossip_peers_response_peers_item",
    "GetLogRootResponse": ".get_log_root_response",
    "GossipExchangeResponse": ".gossip_exchange_response",
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
    "AddGossipPeerResponse",
    "AddToLogResponse",
    "GetGossipAlertsResponse",
    "GetGossipPeersResponse",
    "GetGossipPeersResponsePeersItem",
    "GetLogRootResponse",
    "GossipExchangeResponse",
]
