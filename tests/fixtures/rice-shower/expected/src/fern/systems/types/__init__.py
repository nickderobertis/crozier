



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_system_request_heaters_item import CreateSystemRequestHeatersItem
    from .create_system_request_thermos_item import CreateSystemRequestThermosItem
    from .create_system_response import CreateSystemResponse
    from .create_system_response_heaters_item import CreateSystemResponseHeatersItem
    from .create_system_response_thermos_item import CreateSystemResponseThermosItem
    from .delete_system_response import DeleteSystemResponse
    from .get_system_response import GetSystemResponse
    from .get_system_response_heaters_item import GetSystemResponseHeatersItem
    from .get_system_response_thermos_item import GetSystemResponseThermosItem
    from .list_systems_response_item import ListSystemsResponseItem
    from .list_systems_response_item_heaters_item import ListSystemsResponseItemHeatersItem
    from .list_systems_response_item_thermos_item import ListSystemsResponseItemThermosItem
    from .update_system_request_heaters_item import UpdateSystemRequestHeatersItem
    from .update_system_request_thermos_item import UpdateSystemRequestThermosItem
    from .update_system_response import UpdateSystemResponse
    from .update_system_response_heaters_item import UpdateSystemResponseHeatersItem
    from .update_system_response_thermos_item import UpdateSystemResponseThermosItem
_dynamic_imports: typing.Dict[str, str] = {
    "CreateSystemRequestHeatersItem": ".create_system_request_heaters_item",
    "CreateSystemRequestThermosItem": ".create_system_request_thermos_item",
    "CreateSystemResponse": ".create_system_response",
    "CreateSystemResponseHeatersItem": ".create_system_response_heaters_item",
    "CreateSystemResponseThermosItem": ".create_system_response_thermos_item",
    "DeleteSystemResponse": ".delete_system_response",
    "GetSystemResponse": ".get_system_response",
    "GetSystemResponseHeatersItem": ".get_system_response_heaters_item",
    "GetSystemResponseThermosItem": ".get_system_response_thermos_item",
    "ListSystemsResponseItem": ".list_systems_response_item",
    "ListSystemsResponseItemHeatersItem": ".list_systems_response_item_heaters_item",
    "ListSystemsResponseItemThermosItem": ".list_systems_response_item_thermos_item",
    "UpdateSystemRequestHeatersItem": ".update_system_request_heaters_item",
    "UpdateSystemRequestThermosItem": ".update_system_request_thermos_item",
    "UpdateSystemResponse": ".update_system_response",
    "UpdateSystemResponseHeatersItem": ".update_system_response_heaters_item",
    "UpdateSystemResponseThermosItem": ".update_system_response_thermos_item",
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
    "CreateSystemRequestHeatersItem",
    "CreateSystemRequestThermosItem",
    "CreateSystemResponse",
    "CreateSystemResponseHeatersItem",
    "CreateSystemResponseThermosItem",
    "DeleteSystemResponse",
    "GetSystemResponse",
    "GetSystemResponseHeatersItem",
    "GetSystemResponseThermosItem",
    "ListSystemsResponseItem",
    "ListSystemsResponseItemHeatersItem",
    "ListSystemsResponseItemThermosItem",
    "UpdateSystemRequestHeatersItem",
    "UpdateSystemRequestThermosItem",
    "UpdateSystemResponse",
    "UpdateSystemResponseHeatersItem",
    "UpdateSystemResponseThermosItem",
]
