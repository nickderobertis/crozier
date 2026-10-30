



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_servers_from_strata_mcp_server_strata_strata_id_servers_delete_request_servers_item import (
        DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItem,
    )
    from .delete_servers_from_strata_mcp_server_strata_strata_id_servers_delete_request_servers_item_one import (
        DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItemOne,
    )
    from .set_auth_request_auth_data import SetAuthRequestAuthData
    from .strata_add_servers_request_servers import StrataAddServersRequestServers
    from .strata_add_servers_request_servers_one import StrataAddServersRequestServersOne
    from .strata_create_request_servers import StrataCreateRequestServers
    from .strata_create_request_servers_one import StrataCreateRequestServersOne
    from .strata_set_auth_request_auth_data import StrataSetAuthRequestAuthData
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItem": ".delete_servers_from_strata_mcp_server_strata_strata_id_servers_delete_request_servers_item",
    "DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItemOne": ".delete_servers_from_strata_mcp_server_strata_strata_id_servers_delete_request_servers_item_one",
    "SetAuthRequestAuthData": ".set_auth_request_auth_data",
    "StrataAddServersRequestServers": ".strata_add_servers_request_servers",
    "StrataAddServersRequestServersOne": ".strata_add_servers_request_servers_one",
    "StrataCreateRequestServers": ".strata_create_request_servers",
    "StrataCreateRequestServersOne": ".strata_create_request_servers_one",
    "StrataSetAuthRequestAuthData": ".strata_set_auth_request_auth_data",
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
    "DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItem",
    "DeleteServersFromStrataMcpServerStrataStrataIdServersDeleteRequestServersItemOne",
    "SetAuthRequestAuthData",
    "StrataAddServersRequestServers",
    "StrataAddServersRequestServersOne",
    "StrataCreateRequestServers",
    "StrataCreateRequestServersOne",
    "StrataSetAuthRequestAuthData",
]
