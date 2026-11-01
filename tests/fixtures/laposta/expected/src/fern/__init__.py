



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Campaign,
        CampaignContent,
        CampaignContentCampaign,
        CampaignContentCampaignReport,
        CampaignEnvelope,
        CampaignList,
        Error,
        ErrorError,
        ErrorErrorType,
        Field,
        FieldDatatype,
        FieldDatatypeDisplay,
        FieldEnvelope,
        FieldList,
        FieldState,
        History,
        HistoryDataItem,
        HistoryDataItemEvent,
        HistoryFilters,
        HistoryOrder,
        HistoryOrderOrder,
        HistoryPagination,
        List,
        ListEnvelope,
        ListList,
        ListState,
        Member,
        MemberEnvelope,
        MemberList,
        MemberState,
        Report,
        ReportEnvelope,
        ReportList,
        Segment,
        SegmentEnvelope,
        SegmentList,
        SegmentState,
        SyncResult,
        SyncResultReport,
        Webhook,
        WebhookEnvelope,
        WebhookEvent,
        WebhookList,
        WebhookState,
    )
    from .errors import BadRequestError, TooManyRequestsError, UnauthorizedError
    from . import campaigns, fields, lists, results, segments, subscribers, webhooks
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .campaigns import CampagnegeschiedenisOpvragenRequestOrder
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .fields import (
        VeldToevoegenRequestDatatype,
        VeldToevoegenRequestDatatypeDisplay,
        VeldWijzigenRequestDatatype,
        VeldWijzigenRequestDatatypeDisplay,
    )
    from .subscribers import (
        AlleRelatiesOpvragenRequestState,
        RelatieWijzigenRequestState,
        RelatiegeschiedenisOpvragenRequestOrder,
    )
    from .version import __version__
    from .webhooks import WebhookToevoegenRequestEvent, WebhookWijzigenRequestEvent
_dynamic_imports: typing.Dict[str, str] = {
    "AlleRelatiesOpvragenRequestState": ".subscribers",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CampagnegeschiedenisOpvragenRequestOrder": ".campaigns",
    "Campaign": ".types",
    "CampaignContent": ".types",
    "CampaignContentCampaign": ".types",
    "CampaignContentCampaignReport": ".types",
    "CampaignEnvelope": ".types",
    "CampaignList": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "ErrorError": ".types",
    "ErrorErrorType": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "Field": ".types",
    "FieldDatatype": ".types",
    "FieldDatatypeDisplay": ".types",
    "FieldEnvelope": ".types",
    "FieldList": ".types",
    "FieldState": ".types",
    "History": ".types",
    "HistoryDataItem": ".types",
    "HistoryDataItemEvent": ".types",
    "HistoryFilters": ".types",
    "HistoryOrder": ".types",
    "HistoryOrderOrder": ".types",
    "HistoryPagination": ".types",
    "List": ".types",
    "ListEnvelope": ".types",
    "ListList": ".types",
    "ListState": ".types",
    "Member": ".types",
    "MemberEnvelope": ".types",
    "MemberList": ".types",
    "MemberState": ".types",
    "RelatieWijzigenRequestState": ".subscribers",
    "RelatiegeschiedenisOpvragenRequestOrder": ".subscribers",
    "Report": ".types",
    "ReportEnvelope": ".types",
    "ReportList": ".types",
    "Segment": ".types",
    "SegmentEnvelope": ".types",
    "SegmentList": ".types",
    "SegmentState": ".types",
    "SyncResult": ".types",
    "SyncResultReport": ".types",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "VeldToevoegenRequestDatatype": ".fields",
    "VeldToevoegenRequestDatatypeDisplay": ".fields",
    "VeldWijzigenRequestDatatype": ".fields",
    "VeldWijzigenRequestDatatypeDisplay": ".fields",
    "Webhook": ".types",
    "WebhookEnvelope": ".types",
    "WebhookEvent": ".types",
    "WebhookList": ".types",
    "WebhookState": ".types",
    "WebhookToevoegenRequestEvent": ".webhooks",
    "WebhookWijzigenRequestEvent": ".webhooks",
    "__version__": ".version",
    "campaigns": ".campaigns",
    "fields": ".fields",
    "lists": ".lists",
    "results": ".results",
    "segments": ".segments",
    "subscribers": ".subscribers",
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
    "AlleRelatiesOpvragenRequestState",
    "AsyncFernApi",
    "BadRequestError",
    "CampagnegeschiedenisOpvragenRequestOrder",
    "Campaign",
    "CampaignContent",
    "CampaignContentCampaign",
    "CampaignContentCampaignReport",
    "CampaignEnvelope",
    "CampaignList",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "ErrorError",
    "ErrorErrorType",
    "FernApi",
    "FernApiEnvironment",
    "Field",
    "FieldDatatype",
    "FieldDatatypeDisplay",
    "FieldEnvelope",
    "FieldList",
    "FieldState",
    "History",
    "HistoryDataItem",
    "HistoryDataItemEvent",
    "HistoryFilters",
    "HistoryOrder",
    "HistoryOrderOrder",
    "HistoryPagination",
    "List",
    "ListEnvelope",
    "ListList",
    "ListState",
    "Member",
    "MemberEnvelope",
    "MemberList",
    "MemberState",
    "RelatieWijzigenRequestState",
    "RelatiegeschiedenisOpvragenRequestOrder",
    "Report",
    "ReportEnvelope",
    "ReportList",
    "Segment",
    "SegmentEnvelope",
    "SegmentList",
    "SegmentState",
    "SyncResult",
    "SyncResultReport",
    "TooManyRequestsError",
    "UnauthorizedError",
    "VeldToevoegenRequestDatatype",
    "VeldToevoegenRequestDatatypeDisplay",
    "VeldWijzigenRequestDatatype",
    "VeldWijzigenRequestDatatypeDisplay",
    "Webhook",
    "WebhookEnvelope",
    "WebhookEvent",
    "WebhookList",
    "WebhookState",
    "WebhookToevoegenRequestEvent",
    "WebhookWijzigenRequestEvent",
    "__version__",
    "campaigns",
    "fields",
    "lists",
    "results",
    "segments",
    "subscribers",
    "webhooks",
]
