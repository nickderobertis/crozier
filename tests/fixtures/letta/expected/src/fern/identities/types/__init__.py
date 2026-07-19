



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .list_agents_for_identity_request_include_item import ListAgentsForIdentityRequestIncludeItem
    from .list_agents_for_identity_request_order import ListAgentsForIdentityRequestOrder
    from .list_agents_for_identity_request_order_by import ListAgentsForIdentityRequestOrderBy
    from .list_blocks_for_identity_request_order import ListBlocksForIdentityRequestOrder
    from .list_blocks_for_identity_request_order_by import ListBlocksForIdentityRequestOrderBy
    from .list_identities_request_order import ListIdentitiesRequestOrder
    from .list_identities_request_order_by import ListIdentitiesRequestOrderBy
_dynamic_imports: typing.Dict[str, str] = {
    "ListAgentsForIdentityRequestIncludeItem": ".list_agents_for_identity_request_include_item",
    "ListAgentsForIdentityRequestOrder": ".list_agents_for_identity_request_order",
    "ListAgentsForIdentityRequestOrderBy": ".list_agents_for_identity_request_order_by",
    "ListBlocksForIdentityRequestOrder": ".list_blocks_for_identity_request_order",
    "ListBlocksForIdentityRequestOrderBy": ".list_blocks_for_identity_request_order_by",
    "ListIdentitiesRequestOrder": ".list_identities_request_order",
    "ListIdentitiesRequestOrderBy": ".list_identities_request_order_by",
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
    "ListAgentsForIdentityRequestIncludeItem",
    "ListAgentsForIdentityRequestOrder",
    "ListAgentsForIdentityRequestOrderBy",
    "ListBlocksForIdentityRequestOrder",
    "ListBlocksForIdentityRequestOrderBy",
    "ListIdentitiesRequestOrder",
    "ListIdentitiesRequestOrderBy",
]
