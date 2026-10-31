



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Artifact,
        ArtifactFormat,
        ArtifactFormats,
        Assignment,
        Authority,
        ChangeLogItem,
        Client,
        Contribution,
        Credential,
        ErrorField,
        ErrorResponse,
        EventType,
        Export,
        ExportSummary,
        Flag,
        Form,
        FormField,
        FormResponse,
        Group,
        LatLong,
        LinkedProfile,
        Media,
        MediaUsage,
        ModerationAction,
        ModerationHistoryItem,
        ModerationState,
        NotificationPreview,
        OauthScope,
        OsmId,
        Place,
        Subscription,
        SubscriptionSubmission,
        SubscriptionType,
        Tag,
        TagSet,
        User,
        Via,
    )
    from .errors import BadRequestError, ForbiddenError, InternalServerError, NotFoundError, UnauthorizedError
    from . import assignment, auth, contribution, form, info, media, notifications, subscriptions, tag, user
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Artifact": ".types",
    "ArtifactFormat": ".types",
    "ArtifactFormats": ".types",
    "Assignment": ".types",
    "AsyncFernApi": ".client",
    "Authority": ".types",
    "BadRequestError": ".errors",
    "ChangeLogItem": ".types",
    "Client": ".types",
    "Contribution": ".types",
    "Credential": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorField": ".types",
    "ErrorResponse": ".types",
    "EventType": ".types",
    "Export": ".types",
    "ExportSummary": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Flag": ".types",
    "ForbiddenError": ".errors",
    "Form": ".types",
    "FormField": ".types",
    "FormResponse": ".types",
    "Group": ".types",
    "InternalServerError": ".errors",
    "LatLong": ".types",
    "LinkedProfile": ".types",
    "Media": ".types",
    "MediaUsage": ".types",
    "ModerationAction": ".types",
    "ModerationHistoryItem": ".types",
    "ModerationState": ".types",
    "NotFoundError": ".errors",
    "NotificationPreview": ".types",
    "OauthScope": ".types",
    "OsmId": ".types",
    "Place": ".types",
    "Subscription": ".types",
    "SubscriptionSubmission": ".types",
    "SubscriptionType": ".types",
    "Tag": ".types",
    "TagSet": ".types",
    "UnauthorizedError": ".errors",
    "User": ".types",
    "Via": ".types",
    "__version__": ".version",
    "assignment": ".assignment",
    "auth": ".auth",
    "contribution": ".contribution",
    "form": ".form",
    "info": ".info",
    "media": ".media",
    "notifications": ".notifications",
    "subscriptions": ".subscriptions",
    "tag": ".tag",
    "user": ".user",
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
    "Artifact",
    "ArtifactFormat",
    "ArtifactFormats",
    "Assignment",
    "AsyncFernApi",
    "Authority",
    "BadRequestError",
    "ChangeLogItem",
    "Client",
    "Contribution",
    "Credential",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorField",
    "ErrorResponse",
    "EventType",
    "Export",
    "ExportSummary",
    "FernApi",
    "FernApiEnvironment",
    "Flag",
    "ForbiddenError",
    "Form",
    "FormField",
    "FormResponse",
    "Group",
    "InternalServerError",
    "LatLong",
    "LinkedProfile",
    "Media",
    "MediaUsage",
    "ModerationAction",
    "ModerationHistoryItem",
    "ModerationState",
    "NotFoundError",
    "NotificationPreview",
    "OauthScope",
    "OsmId",
    "Place",
    "Subscription",
    "SubscriptionSubmission",
    "SubscriptionType",
    "Tag",
    "TagSet",
    "UnauthorizedError",
    "User",
    "Via",
    "__version__",
    "assignment",
    "auth",
    "contribution",
    "form",
    "info",
    "media",
    "notifications",
    "subscriptions",
    "tag",
    "user",
]
