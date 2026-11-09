



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CreateLiveActivityJobRequest,
        LiveActivityAction,
        LiveActivityActivityIdScope,
        LiveActivityEndJobRequest,
        LiveActivityEndJobRequestAction,
        LiveActivityJobResponse,
        LiveActivityJobResponseStatus,
        LiveActivityJobTarget,
        LiveActivityOptions,
        LiveActivityOptionsAlert,
        LiveActivityOptionsDismissalDate,
        LiveActivityOptionsExpiration,
        LiveActivityOptionsPriority,
        LiveActivityOptionsPriorityZero,
        LiveActivityOptionsStaleDate,
        LiveActivityOptionsTimestamp,
        LiveActivityScopedLookup,
        LiveActivityStartJobRequest,
        LiveActivityStartJobRequestAction,
        LiveActivityToken,
        LiveActivityTokenType,
        LiveActivityTopicScope,
        LiveActivityUpdateJobRequest,
        LiveActivityUpdateJobRequestAction,
        LiveActivityUserScope,
        LiveActivityUserTopicSubscription,
        NotificationPayload,
        NotificationPayloadPriority,
        PaginatedPublishJobs,
        PaginatedTopicSubscribers,
        PaginatedUsers,
        Platform,
        PublishJob,
        PublishJobStatus,
        QueuedJobResponse,
        SendNotificationRequest,
        Token,
        Topic,
        TopicSubscriber,
        User,
        UserTopicSubscription,
    )
    from .errors import BadRequestError, ConflictError, InternalServerError, NotFoundError, ServiceUnavailableError
    from . import health, live_activity, notifications, subscriptions, tokens, topics, users
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .live_activity import PostV1LiveActivityTokensResponse
    from .notifications import GetV1TopicsTopicIdNotificationsRequestStatus, GetV1UsersUserIdNotificationsRequestStatus
    from .tokens import PostV1UsersTokensResponse
    from .topics import GetV1TopicsTopicIdCountResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "ConflictError": ".errors",
    "CreateLiveActivityJobRequest": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetV1TopicsTopicIdCountResponse": ".topics",
    "GetV1TopicsTopicIdNotificationsRequestStatus": ".notifications",
    "GetV1UsersUserIdNotificationsRequestStatus": ".notifications",
    "InternalServerError": ".errors",
    "LiveActivityAction": ".types",
    "LiveActivityActivityIdScope": ".types",
    "LiveActivityEndJobRequest": ".types",
    "LiveActivityEndJobRequestAction": ".types",
    "LiveActivityJobResponse": ".types",
    "LiveActivityJobResponseStatus": ".types",
    "LiveActivityJobTarget": ".types",
    "LiveActivityOptions": ".types",
    "LiveActivityOptionsAlert": ".types",
    "LiveActivityOptionsDismissalDate": ".types",
    "LiveActivityOptionsExpiration": ".types",
    "LiveActivityOptionsPriority": ".types",
    "LiveActivityOptionsPriorityZero": ".types",
    "LiveActivityOptionsStaleDate": ".types",
    "LiveActivityOptionsTimestamp": ".types",
    "LiveActivityScopedLookup": ".types",
    "LiveActivityStartJobRequest": ".types",
    "LiveActivityStartJobRequestAction": ".types",
    "LiveActivityToken": ".types",
    "LiveActivityTokenType": ".types",
    "LiveActivityTopicScope": ".types",
    "LiveActivityUpdateJobRequest": ".types",
    "LiveActivityUpdateJobRequestAction": ".types",
    "LiveActivityUserScope": ".types",
    "LiveActivityUserTopicSubscription": ".types",
    "NotFoundError": ".errors",
    "NotificationPayload": ".types",
    "NotificationPayloadPriority": ".types",
    "PaginatedPublishJobs": ".types",
    "PaginatedTopicSubscribers": ".types",
    "PaginatedUsers": ".types",
    "Platform": ".types",
    "PostV1LiveActivityTokensResponse": ".live_activity",
    "PostV1UsersTokensResponse": ".tokens",
    "PublishJob": ".types",
    "PublishJobStatus": ".types",
    "QueuedJobResponse": ".types",
    "SendNotificationRequest": ".types",
    "ServiceUnavailableError": ".errors",
    "Token": ".types",
    "Topic": ".types",
    "TopicSubscriber": ".types",
    "User": ".types",
    "UserTopicSubscription": ".types",
    "__version__": ".version",
    "health": ".health",
    "live_activity": ".live_activity",
    "notifications": ".notifications",
    "subscriptions": ".subscriptions",
    "tokens": ".tokens",
    "topics": ".topics",
    "users": ".users",
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
    "ConflictError",
    "CreateLiveActivityJobRequest",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "GetV1TopicsTopicIdCountResponse",
    "GetV1TopicsTopicIdNotificationsRequestStatus",
    "GetV1UsersUserIdNotificationsRequestStatus",
    "InternalServerError",
    "LiveActivityAction",
    "LiveActivityActivityIdScope",
    "LiveActivityEndJobRequest",
    "LiveActivityEndJobRequestAction",
    "LiveActivityJobResponse",
    "LiveActivityJobResponseStatus",
    "LiveActivityJobTarget",
    "LiveActivityOptions",
    "LiveActivityOptionsAlert",
    "LiveActivityOptionsDismissalDate",
    "LiveActivityOptionsExpiration",
    "LiveActivityOptionsPriority",
    "LiveActivityOptionsPriorityZero",
    "LiveActivityOptionsStaleDate",
    "LiveActivityOptionsTimestamp",
    "LiveActivityScopedLookup",
    "LiveActivityStartJobRequest",
    "LiveActivityStartJobRequestAction",
    "LiveActivityToken",
    "LiveActivityTokenType",
    "LiveActivityTopicScope",
    "LiveActivityUpdateJobRequest",
    "LiveActivityUpdateJobRequestAction",
    "LiveActivityUserScope",
    "LiveActivityUserTopicSubscription",
    "NotFoundError",
    "NotificationPayload",
    "NotificationPayloadPriority",
    "PaginatedPublishJobs",
    "PaginatedTopicSubscribers",
    "PaginatedUsers",
    "Platform",
    "PostV1LiveActivityTokensResponse",
    "PostV1UsersTokensResponse",
    "PublishJob",
    "PublishJobStatus",
    "QueuedJobResponse",
    "SendNotificationRequest",
    "ServiceUnavailableError",
    "Token",
    "Topic",
    "TopicSubscriber",
    "User",
    "UserTopicSubscription",
    "__version__",
    "health",
    "live_activity",
    "notifications",
    "subscriptions",
    "tokens",
    "topics",
    "users",
]
