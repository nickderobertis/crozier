



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_mcp_server_request import AddMcpServerRequest
    from .add_mcp_server_response_item import AddMcpServerResponseItem
    from .connect_mcp_server_request import ConnectMcpServerRequest
    from .delete_mcp_server_response_item import DeleteMcpServerResponseItem
    from .list_mcp_servers_response_value import ListMcpServersResponseValue
    from .list_tools_request_order import ListToolsRequestOrder
    from .list_tools_request_order_by import ListToolsRequestOrderBy
    from .test_mcp_server_request import TestMcpServerRequest
    from .tool_search_request_search_mode import ToolSearchRequestSearchMode
    from .update_mcp_server_request_body import UpdateMcpServerRequestBody
    from .update_mcp_server_response import UpdateMcpServerResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AddMcpServerRequest": ".add_mcp_server_request",
    "AddMcpServerResponseItem": ".add_mcp_server_response_item",
    "ConnectMcpServerRequest": ".connect_mcp_server_request",
    "DeleteMcpServerResponseItem": ".delete_mcp_server_response_item",
    "ListMcpServersResponseValue": ".list_mcp_servers_response_value",
    "ListToolsRequestOrder": ".list_tools_request_order",
    "ListToolsRequestOrderBy": ".list_tools_request_order_by",
    "TestMcpServerRequest": ".test_mcp_server_request",
    "ToolSearchRequestSearchMode": ".tool_search_request_search_mode",
    "UpdateMcpServerRequestBody": ".update_mcp_server_request_body",
    "UpdateMcpServerResponse": ".update_mcp_server_response",
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
    "AddMcpServerRequest",
    "AddMcpServerResponseItem",
    "ConnectMcpServerRequest",
    "DeleteMcpServerResponseItem",
    "ListMcpServersResponseValue",
    "ListToolsRequestOrder",
    "ListToolsRequestOrderBy",
    "TestMcpServerRequest",
    "ToolSearchRequestSearchMode",
    "UpdateMcpServerRequestBody",
    "UpdateMcpServerResponse",
]
