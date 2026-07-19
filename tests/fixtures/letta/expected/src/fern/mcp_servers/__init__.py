



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateMcpServerRequestConfig,
        CreateMcpServerRequestConfig_Sse,
        CreateMcpServerRequestConfig_Stdio,
        CreateMcpServerRequestConfig_StreamableHttp,
        McpCreateMcpServerResponse,
        McpCreateMcpServerResponse_Sse,
        McpCreateMcpServerResponse_Stdio,
        McpCreateMcpServerResponse_StreamableHttp,
        McpListMcpServersResponseItem,
        McpListMcpServersResponseItem_Sse,
        McpListMcpServersResponseItem_Stdio,
        McpListMcpServersResponseItem_StreamableHttp,
        McpRetrieveMcpServerResponse,
        McpRetrieveMcpServerResponse_Sse,
        McpRetrieveMcpServerResponse_Stdio,
        McpRetrieveMcpServerResponse_StreamableHttp,
        McpUpdateMcpServerResponse,
        McpUpdateMcpServerResponse_Sse,
        McpUpdateMcpServerResponse_Stdio,
        McpUpdateMcpServerResponse_StreamableHttp,
        UpdateMcpServerRequestConfig,
        UpdateMcpServerRequestConfig_Sse,
        UpdateMcpServerRequestConfig_Stdio,
        UpdateMcpServerRequestConfig_StreamableHttp,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CreateMcpServerRequestConfig": ".types",
    "CreateMcpServerRequestConfig_Sse": ".types",
    "CreateMcpServerRequestConfig_Stdio": ".types",
    "CreateMcpServerRequestConfig_StreamableHttp": ".types",
    "McpCreateMcpServerResponse": ".types",
    "McpCreateMcpServerResponse_Sse": ".types",
    "McpCreateMcpServerResponse_Stdio": ".types",
    "McpCreateMcpServerResponse_StreamableHttp": ".types",
    "McpListMcpServersResponseItem": ".types",
    "McpListMcpServersResponseItem_Sse": ".types",
    "McpListMcpServersResponseItem_Stdio": ".types",
    "McpListMcpServersResponseItem_StreamableHttp": ".types",
    "McpRetrieveMcpServerResponse": ".types",
    "McpRetrieveMcpServerResponse_Sse": ".types",
    "McpRetrieveMcpServerResponse_Stdio": ".types",
    "McpRetrieveMcpServerResponse_StreamableHttp": ".types",
    "McpUpdateMcpServerResponse": ".types",
    "McpUpdateMcpServerResponse_Sse": ".types",
    "McpUpdateMcpServerResponse_Stdio": ".types",
    "McpUpdateMcpServerResponse_StreamableHttp": ".types",
    "UpdateMcpServerRequestConfig": ".types",
    "UpdateMcpServerRequestConfig_Sse": ".types",
    "UpdateMcpServerRequestConfig_Stdio": ".types",
    "UpdateMcpServerRequestConfig_StreamableHttp": ".types",
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
