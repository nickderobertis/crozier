



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Agent,
        AgentCapabilities,
        AgentSchema,
        ErrorResponse,
        Item,
        ListNamespaceResponse,
        Message,
        MessageContent,
        MessageContentOneItem,
        MessageContentOneItemOne,
        MessageContentOneItemText,
        MessageContentOneItemTextType,
        Run,
        RunCreate,
        RunCreateConfig,
        RunCreateIfNotExists,
        RunCreateInput,
        RunCreateOnCompletion,
        RunCreateOnDisconnect,
        RunStatus,
        RunStream,
        RunStreamStreamMode,
        RunWaitResponse,
        SearchItemsResponse,
        StreamMode,
        StreamingChannel,
        StreamingChannelZero,
        StreamingCommandResponse,
        StreamingCommandResponse_Error,
        StreamingCommandResponse_Success,
        StreamingErrorResponse,
        StreamingEvent,
        StreamingEventType,
        StreamingNamespace,
        StreamingSuccessResponse,
        StreamingSuccessResponseMeta,
        Thread,
        ThreadCheckpoint,
        ThreadState,
        ThreadStatus,
    )
    from .errors import BadRequestError, ConflictError, NotFoundError, UnprocessableEntityError
    from . import agents, background_runs, runs, store, streaming, threads
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .background_runs import CancelRunRequestAction
    from .client import AsyncFernApi, FernApi
    from .threads import ThreadCreateIfExists
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Agent": ".types",
    "AgentCapabilities": ".types",
    "AgentSchema": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CancelRunRequestAction": ".background_runs",
    "ConflictError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "FernApi": ".client",
    "Item": ".types",
    "ListNamespaceResponse": ".types",
    "Message": ".types",
    "MessageContent": ".types",
    "MessageContentOneItem": ".types",
    "MessageContentOneItemOne": ".types",
    "MessageContentOneItemText": ".types",
    "MessageContentOneItemTextType": ".types",
    "NotFoundError": ".errors",
    "Run": ".types",
    "RunCreate": ".types",
    "RunCreateConfig": ".types",
    "RunCreateIfNotExists": ".types",
    "RunCreateInput": ".types",
    "RunCreateOnCompletion": ".types",
    "RunCreateOnDisconnect": ".types",
    "RunStatus": ".types",
    "RunStream": ".types",
    "RunStreamStreamMode": ".types",
    "RunWaitResponse": ".types",
    "SearchItemsResponse": ".types",
    "StreamMode": ".types",
    "StreamingChannel": ".types",
    "StreamingChannelZero": ".types",
    "StreamingCommandResponse": ".types",
    "StreamingCommandResponse_Error": ".types",
    "StreamingCommandResponse_Success": ".types",
    "StreamingErrorResponse": ".types",
    "StreamingEvent": ".types",
    "StreamingEventType": ".types",
    "StreamingNamespace": ".types",
    "StreamingSuccessResponse": ".types",
    "StreamingSuccessResponseMeta": ".types",
    "Thread": ".types",
    "ThreadCheckpoint": ".types",
    "ThreadCreateIfExists": ".threads",
    "ThreadState": ".types",
    "ThreadStatus": ".types",
    "UnprocessableEntityError": ".errors",
    "__version__": ".version",
    "agents": ".agents",
    "background_runs": ".background_runs",
    "runs": ".runs",
    "store": ".store",
    "streaming": ".streaming",
    "threads": ".threads",
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
    "Agent",
    "AgentCapabilities",
    "AgentSchema",
    "AsyncFernApi",
    "BadRequestError",
    "CancelRunRequestAction",
    "ConflictError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "FernApi",
    "Item",
    "ListNamespaceResponse",
    "Message",
    "MessageContent",
    "MessageContentOneItem",
    "MessageContentOneItemOne",
    "MessageContentOneItemText",
    "MessageContentOneItemTextType",
    "NotFoundError",
    "Run",
    "RunCreate",
    "RunCreateConfig",
    "RunCreateIfNotExists",
    "RunCreateInput",
    "RunCreateOnCompletion",
    "RunCreateOnDisconnect",
    "RunStatus",
    "RunStream",
    "RunStreamStreamMode",
    "RunWaitResponse",
    "SearchItemsResponse",
    "StreamMode",
    "StreamingChannel",
    "StreamingChannelZero",
    "StreamingCommandResponse",
    "StreamingCommandResponse_Error",
    "StreamingCommandResponse_Success",
    "StreamingErrorResponse",
    "StreamingEvent",
    "StreamingEventType",
    "StreamingNamespace",
    "StreamingSuccessResponse",
    "StreamingSuccessResponseMeta",
    "Thread",
    "ThreadCheckpoint",
    "ThreadCreateIfExists",
    "ThreadState",
    "ThreadStatus",
    "UnprocessableEntityError",
    "__version__",
    "agents",
    "background_runs",
    "runs",
    "store",
    "streaming",
    "threads",
]
