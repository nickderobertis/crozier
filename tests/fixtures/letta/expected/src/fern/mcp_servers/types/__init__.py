



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_mcp_server_request_config import (
        CreateMcpServerRequestConfig,
        CreateMcpServerRequestConfig_Sse,
        CreateMcpServerRequestConfig_Stdio,
        CreateMcpServerRequestConfig_StreamableHttp,
    )
    from .mcp_create_mcp_server_response import (
        McpCreateMcpServerResponse,
        McpCreateMcpServerResponse_Sse,
        McpCreateMcpServerResponse_Stdio,
        McpCreateMcpServerResponse_StreamableHttp,
    )
    from .mcp_list_mcp_servers_response_item import (
        McpListMcpServersResponseItem,
        McpListMcpServersResponseItem_Sse,
        McpListMcpServersResponseItem_Stdio,
        McpListMcpServersResponseItem_StreamableHttp,
    )
    from .mcp_retrieve_mcp_server_response import (
        McpRetrieveMcpServerResponse,
        McpRetrieveMcpServerResponse_Sse,
        McpRetrieveMcpServerResponse_Stdio,
        McpRetrieveMcpServerResponse_StreamableHttp,
    )
    from .mcp_update_mcp_server_response import (
        McpUpdateMcpServerResponse,
        McpUpdateMcpServerResponse_Sse,
        McpUpdateMcpServerResponse_Stdio,
        McpUpdateMcpServerResponse_StreamableHttp,
    )
    from .update_mcp_server_request_config import (
        UpdateMcpServerRequestConfig,
        UpdateMcpServerRequestConfig_Sse,
        UpdateMcpServerRequestConfig_Stdio,
        UpdateMcpServerRequestConfig_StreamableHttp,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateMcpServerRequestConfig": ".create_mcp_server_request_config",
    "CreateMcpServerRequestConfig_Sse": ".create_mcp_server_request_config",
    "CreateMcpServerRequestConfig_Stdio": ".create_mcp_server_request_config",
    "CreateMcpServerRequestConfig_StreamableHttp": ".create_mcp_server_request_config",
    "McpCreateMcpServerResponse": ".mcp_create_mcp_server_response",
    "McpCreateMcpServerResponse_Sse": ".mcp_create_mcp_server_response",
    "McpCreateMcpServerResponse_Stdio": ".mcp_create_mcp_server_response",
    "McpCreateMcpServerResponse_StreamableHttp": ".mcp_create_mcp_server_response",
    "McpListMcpServersResponseItem": ".mcp_list_mcp_servers_response_item",
    "McpListMcpServersResponseItem_Sse": ".mcp_list_mcp_servers_response_item",
    "McpListMcpServersResponseItem_Stdio": ".mcp_list_mcp_servers_response_item",
    "McpListMcpServersResponseItem_StreamableHttp": ".mcp_list_mcp_servers_response_item",
    "McpRetrieveMcpServerResponse": ".mcp_retrieve_mcp_server_response",
    "McpRetrieveMcpServerResponse_Sse": ".mcp_retrieve_mcp_server_response",
    "McpRetrieveMcpServerResponse_Stdio": ".mcp_retrieve_mcp_server_response",
    "McpRetrieveMcpServerResponse_StreamableHttp": ".mcp_retrieve_mcp_server_response",
    "McpUpdateMcpServerResponse": ".mcp_update_mcp_server_response",
    "McpUpdateMcpServerResponse_Sse": ".mcp_update_mcp_server_response",
    "McpUpdateMcpServerResponse_Stdio": ".mcp_update_mcp_server_response",
    "McpUpdateMcpServerResponse_StreamableHttp": ".mcp_update_mcp_server_response",
    "UpdateMcpServerRequestConfig": ".update_mcp_server_request_config",
    "UpdateMcpServerRequestConfig_Sse": ".update_mcp_server_request_config",
    "UpdateMcpServerRequestConfig_Stdio": ".update_mcp_server_request_config",
    "UpdateMcpServerRequestConfig_StreamableHttp": ".update_mcp_server_request_config",
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
    "CreateMcpServerRequestConfig",
    "CreateMcpServerRequestConfig_Sse",
    "CreateMcpServerRequestConfig_Stdio",
    "CreateMcpServerRequestConfig_StreamableHttp",
    "McpCreateMcpServerResponse",
    "McpCreateMcpServerResponse_Sse",
    "McpCreateMcpServerResponse_Stdio",
    "McpCreateMcpServerResponse_StreamableHttp",
    "McpListMcpServersResponseItem",
    "McpListMcpServersResponseItem_Sse",
    "McpListMcpServersResponseItem_Stdio",
    "McpListMcpServersResponseItem_StreamableHttp",
    "McpRetrieveMcpServerResponse",
    "McpRetrieveMcpServerResponse_Sse",
    "McpRetrieveMcpServerResponse_Stdio",
    "McpRetrieveMcpServerResponse_StreamableHttp",
    "McpUpdateMcpServerResponse",
    "McpUpdateMcpServerResponse_Sse",
    "McpUpdateMcpServerResponse_Stdio",
    "McpUpdateMcpServerResponse_StreamableHttp",
    "UpdateMcpServerRequestConfig",
    "UpdateMcpServerRequestConfig_Sse",
    "UpdateMcpServerRequestConfig_Stdio",
    "UpdateMcpServerRequestConfig_StreamableHttp",
]
