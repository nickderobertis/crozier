



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Conversation,
        Delta,
        DeltaEvent,
        Done,
        DoneEvent,
        DoneFinishReason,
        ErrorEvent,
        Message,
        MessageRole,
        MessageStatus,
        ModelAlias,
        Problem,
        StreamEvent,
        StreamEvent_Delta,
        StreamEvent_Done,
        StreamEvent_Error,
        StreamEvent_Usage,
        Usage,
        UsageEvent,
    )
    from .errors import (
        BadRequestError,
        ContentTooLargeError,
        ForbiddenError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    )
    from . import conversations
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ContentTooLargeError": ".errors",
    "Conversation": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Delta": ".types",
    "DeltaEvent": ".types",
    "Done": ".types",
    "DoneEvent": ".types",
    "DoneFinishReason": ".types",
    "ErrorEvent": ".types",
    "FernApi": ".client",
    "ForbiddenError": ".errors",
    "Message": ".types",
    "MessageRole": ".types",
    "MessageStatus": ".types",
    "ModelAlias": ".types",
    "NotFoundError": ".errors",
    "Problem": ".types",
    "ServiceUnavailableError": ".errors",
    "StreamEvent": ".types",
    "StreamEvent_Delta": ".types",
    "StreamEvent_Done": ".types",
    "StreamEvent_Error": ".types",
    "StreamEvent_Usage": ".types",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "Usage": ".types",
    "UsageEvent": ".types",
    "__version__": ".version",
    "conversations": ".conversations",
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
    "ContentTooLargeError",
    "Conversation",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Delta",
    "DeltaEvent",
    "Done",
    "DoneEvent",
    "DoneFinishReason",
    "ErrorEvent",
    "FernApi",
    "ForbiddenError",
    "Message",
    "MessageRole",
    "MessageStatus",
    "ModelAlias",
    "NotFoundError",
    "Problem",
    "ServiceUnavailableError",
    "StreamEvent",
    "StreamEvent_Delta",
    "StreamEvent_Done",
    "StreamEvent_Error",
    "StreamEvent_Usage",
    "TooManyRequestsError",
    "UnauthorizedError",
    "Usage",
    "UsageEvent",
    "__version__",
    "conversations",
]
