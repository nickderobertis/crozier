



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_connectv1connector_config_response import GetConnectv1ConnectorConfigResponse
    from .inline_object_config import InlineObjectConfig
    from .inline_object_offsets_item import InlineObjectOffsetsItem
    from .list_connectv1connectors_with_expansions_request_expand import (
        ListConnectv1ConnectorsWithExpansionsRequestExpand,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetConnectv1ConnectorConfigResponse": ".get_connectv1connector_config_response",
    "InlineObjectConfig": ".inline_object_config",
    "InlineObjectOffsetsItem": ".inline_object_offsets_item",
    "ListConnectv1ConnectorsWithExpansionsRequestExpand": ".list_connectv1connectors_with_expansions_request_expand",
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
    "GetConnectv1ConnectorConfigResponse",
    "InlineObjectConfig",
    "InlineObjectOffsetsItem",
    "ListConnectv1ConnectorsWithExpansionsRequestExpand",
]
