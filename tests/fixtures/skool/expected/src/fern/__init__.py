



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ChatMessage,
        ErrorResponse,
        ErrorResponseStatus,
        Group,
        Member,
        Post,
        Session,
        Webhook,
        WebhookEventsItem,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError, UnprocessableEntityError
    from . import analytics, chat, groups, members, posts, sessions, webhooks
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .analytics import GetGroupAnalyticsResponse
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
    from .webhooks import CreateWebhookRequestEventsItem
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ChatMessage": ".types",
    "CreateWebhookRequestEventsItem": ".webhooks",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorResponse": ".types",
    "ErrorResponseStatus": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetGroupAnalyticsResponse": ".analytics",
    "Group": ".types",
    "Member": ".types",
    "NotFoundError": ".errors",
    "Post": ".types",
    "Session": ".types",
    "UnauthorizedError": ".errors",
    "UnprocessableEntityError": ".errors",
    "Webhook": ".types",
    "WebhookEventsItem": ".types",
    "__version__": ".version",
    "analytics": ".analytics",
    "chat": ".chat",
    "groups": ".groups",
    "members": ".members",
    "posts": ".posts",
    "sessions": ".sessions",
    "webhooks": ".webhooks",
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
    "ChatMessage",
    "CreateWebhookRequestEventsItem",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorResponse",
    "ErrorResponseStatus",
    "FernApi",
    "FernApiEnvironment",
    "GetGroupAnalyticsResponse",
    "Group",
    "Member",
    "NotFoundError",
    "Post",
    "Session",
    "UnauthorizedError",
    "UnprocessableEntityError",
    "Webhook",
    "WebhookEventsItem",
    "__version__",
    "analytics",
    "chat",
    "groups",
    "members",
    "posts",
    "sessions",
    "webhooks",
]
