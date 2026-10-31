



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .artifact import Artifact
    from .artifact_format import ArtifactFormat
    from .artifact_formats import ArtifactFormats
    from .assignment import Assignment
    from .authority import Authority
    from .change_log_item import ChangeLogItem
    from .client import Client
    from .contribution import Contribution
    from .credential import Credential
    from .error_field import ErrorField
    from .error_response import ErrorResponse
    from .event_type import EventType
    from .export import Export
    from .export_summary import ExportSummary
    from .flag import Flag
    from .form import Form
    from .form_field import FormField
    from .form_response import FormResponse
    from .group import Group
    from .lat_long import LatLong
    from .linked_profile import LinkedProfile
    from .media import Media
    from .media_usage import MediaUsage
    from .moderation_action import ModerationAction
    from .moderation_history_item import ModerationHistoryItem
    from .moderation_state import ModerationState
    from .notification_preview import NotificationPreview
    from .oauth_scope import OauthScope
    from .osm_id import OsmId
    from .place import Place
    from .subscription import Subscription
    from .subscription_submission import SubscriptionSubmission
    from .subscription_type import SubscriptionType
    from .tag import Tag
    from .tag_set import TagSet
    from .user import User
    from .via import Via
_dynamic_imports: typing.Dict[str, str] = {
    "Artifact": ".artifact",
    "ArtifactFormat": ".artifact_format",
    "ArtifactFormats": ".artifact_formats",
    "Assignment": ".assignment",
    "Authority": ".authority",
    "ChangeLogItem": ".change_log_item",
    "Client": ".client",
    "Contribution": ".contribution",
    "Credential": ".credential",
    "ErrorField": ".error_field",
    "ErrorResponse": ".error_response",
    "EventType": ".event_type",
    "Export": ".export",
    "ExportSummary": ".export_summary",
    "Flag": ".flag",
    "Form": ".form",
    "FormField": ".form_field",
    "FormResponse": ".form_response",
    "Group": ".group",
    "LatLong": ".lat_long",
    "LinkedProfile": ".linked_profile",
    "Media": ".media",
    "MediaUsage": ".media_usage",
    "ModerationAction": ".moderation_action",
    "ModerationHistoryItem": ".moderation_history_item",
    "ModerationState": ".moderation_state",
    "NotificationPreview": ".notification_preview",
    "OauthScope": ".oauth_scope",
    "OsmId": ".osm_id",
    "Place": ".place",
    "Subscription": ".subscription",
    "SubscriptionSubmission": ".subscription_submission",
    "SubscriptionType": ".subscription_type",
    "Tag": ".tag",
    "TagSet": ".tag_set",
    "User": ".user",
    "Via": ".via",
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
    "Authority",
    "ChangeLogItem",
    "Client",
    "Contribution",
    "Credential",
    "ErrorField",
    "ErrorResponse",
    "EventType",
    "Export",
    "ExportSummary",
    "Flag",
    "Form",
    "FormField",
    "FormResponse",
    "Group",
    "LatLong",
    "LinkedProfile",
    "Media",
    "MediaUsage",
    "ModerationAction",
    "ModerationHistoryItem",
    "ModerationState",
    "NotificationPreview",
    "OauthScope",
    "OsmId",
    "Place",
    "Subscription",
    "SubscriptionSubmission",
    "SubscriptionType",
    "Tag",
    "TagSet",
    "User",
    "Via",
]
