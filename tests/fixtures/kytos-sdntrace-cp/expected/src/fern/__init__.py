



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PutV1TraceRequestTrace,
        PutV1TraceRequestTraceEth,
        PutV1TraceRequestTraceIp,
        PutV1TraceRequestTraceSwitch,
        PutV1TraceRequestTraceTp,
        PutV1TraceResponse,
        PutV1TraceResponseResultItem,
        PutV1TraceResponseResultItemType,
        PutV1TracesRequestItem,
        PutV1TracesRequestItemTrace,
        PutV1TracesRequestItemTraceEth,
        PutV1TracesRequestItemTraceIp,
        PutV1TracesRequestItemTraceSwitch,
        PutV1TracesRequestItemTraceTp,
        PutV1TracesResponse,
        PutV1TracesResponseResultItemItem,
        PutV1TracesResponseResultItemItemType,
    )
    from .errors import BadRequestError, FailedDependencyError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FailedDependencyError": ".errors",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "PutV1TraceRequestTrace": ".types",
    "PutV1TraceRequestTraceEth": ".types",
    "PutV1TraceRequestTraceIp": ".types",
    "PutV1TraceRequestTraceSwitch": ".types",
    "PutV1TraceRequestTraceTp": ".types",
    "PutV1TraceResponse": ".types",
    "PutV1TraceResponseResultItem": ".types",
    "PutV1TraceResponseResultItemType": ".types",
    "PutV1TracesRequestItem": ".types",
    "PutV1TracesRequestItemTrace": ".types",
    "PutV1TracesRequestItemTraceEth": ".types",
    "PutV1TracesRequestItemTraceIp": ".types",
    "PutV1TracesRequestItemTraceSwitch": ".types",
    "PutV1TracesRequestItemTraceTp": ".types",
    "PutV1TracesResponse": ".types",
    "PutV1TracesResponseResultItemItem": ".types",
    "PutV1TracesResponseResultItemItemType": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "BadRequestError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FailedDependencyError",
    "FernApi",
    "FernApiEnvironment",
    "PutV1TraceRequestTrace",
    "PutV1TraceRequestTraceEth",
    "PutV1TraceRequestTraceIp",
    "PutV1TraceRequestTraceSwitch",
    "PutV1TraceRequestTraceTp",
    "PutV1TraceResponse",
    "PutV1TraceResponseResultItem",
    "PutV1TraceResponseResultItemType",
    "PutV1TracesRequestItem",
    "PutV1TracesRequestItemTrace",
    "PutV1TracesRequestItemTraceEth",
    "PutV1TracesRequestItemTraceIp",
    "PutV1TracesRequestItemTraceSwitch",
    "PutV1TracesRequestItemTraceTp",
    "PutV1TracesResponse",
    "PutV1TracesResponseResultItemItem",
    "PutV1TracesResponseResultItemItemType",
    "__version__",
]
