



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .channel_ingress_approve_response import ChannelIngressApproveResponse
    from .channel_ingress_list_response import ChannelIngressListResponse
    from .channel_ingress_list_response_problems_item import ChannelIngressListResponseProblemsItem
    from .channel_ingress_list_response_sources_item import ChannelIngressListResponseSourcesItem
    from .channel_ingress_list_response_sources_item_routes_item import ChannelIngressListResponseSourcesItemRoutesItem
    from .channel_ingress_list_response_sources_item_routes_item_verification import (
        ChannelIngressListResponseSourcesItemRoutesItemVerification,
    )
    from .channel_ingress_list_response_sources_item_state import ChannelIngressListResponseSourcesItemState
    from .channel_ingress_revoke_response import ChannelIngressRevokeResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ChannelIngressApproveResponse": ".channel_ingress_approve_response",
    "ChannelIngressListResponse": ".channel_ingress_list_response",
    "ChannelIngressListResponseProblemsItem": ".channel_ingress_list_response_problems_item",
    "ChannelIngressListResponseSourcesItem": ".channel_ingress_list_response_sources_item",
    "ChannelIngressListResponseSourcesItemRoutesItem": ".channel_ingress_list_response_sources_item_routes_item",
    "ChannelIngressListResponseSourcesItemRoutesItemVerification": ".channel_ingress_list_response_sources_item_routes_item_verification",
    "ChannelIngressListResponseSourcesItemState": ".channel_ingress_list_response_sources_item_state",
    "ChannelIngressRevokeResponse": ".channel_ingress_revoke_response",
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
    "ChannelIngressApproveResponse",
    "ChannelIngressListResponse",
    "ChannelIngressListResponseProblemsItem",
    "ChannelIngressListResponseSourcesItem",
    "ChannelIngressListResponseSourcesItemRoutesItem",
    "ChannelIngressListResponseSourcesItemRoutesItemVerification",
    "ChannelIngressListResponseSourcesItemState",
    "ChannelIngressRevokeResponse",
]
