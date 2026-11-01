



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .campaign import Campaign
    from .campaign_content import CampaignContent
    from .campaign_content_campaign import CampaignContentCampaign
    from .campaign_content_campaign_report import CampaignContentCampaignReport
    from .campaign_envelope import CampaignEnvelope
    from .campaign_list import CampaignList
    from .error import Error
    from .error_error import ErrorError
    from .error_error_type import ErrorErrorType
    from .field import Field
    from .field_datatype import FieldDatatype
    from .field_datatype_display import FieldDatatypeDisplay
    from .field_envelope import FieldEnvelope
    from .field_list import FieldList
    from .field_state import FieldState
    from .history import History
    from .history_data_item import HistoryDataItem
    from .history_data_item_event import HistoryDataItemEvent
    from .history_filters import HistoryFilters
    from .history_order import HistoryOrder
    from .history_order_order import HistoryOrderOrder
    from .history_pagination import HistoryPagination
    from .list_ import List
    from .list_envelope import ListEnvelope
    from .list_list import ListList
    from .list_state import ListState
    from .member import Member
    from .member_envelope import MemberEnvelope
    from .member_list import MemberList
    from .member_state import MemberState
    from .report import Report
    from .report_envelope import ReportEnvelope
    from .report_list import ReportList
    from .segment import Segment
    from .segment_envelope import SegmentEnvelope
    from .segment_list import SegmentList
    from .segment_state import SegmentState
    from .sync_result import SyncResult
    from .sync_result_report import SyncResultReport
    from .webhook import Webhook
    from .webhook_envelope import WebhookEnvelope
    from .webhook_event import WebhookEvent
    from .webhook_list import WebhookList
    from .webhook_state import WebhookState
_dynamic_imports: typing.Dict[str, str] = {
    "Campaign": ".campaign",
    "CampaignContent": ".campaign_content",
    "CampaignContentCampaign": ".campaign_content_campaign",
    "CampaignContentCampaignReport": ".campaign_content_campaign_report",
    "CampaignEnvelope": ".campaign_envelope",
    "CampaignList": ".campaign_list",
    "Error": ".error",
    "ErrorError": ".error_error",
    "ErrorErrorType": ".error_error_type",
    "Field": ".field",
    "FieldDatatype": ".field_datatype",
    "FieldDatatypeDisplay": ".field_datatype_display",
    "FieldEnvelope": ".field_envelope",
    "FieldList": ".field_list",
    "FieldState": ".field_state",
    "History": ".history",
    "HistoryDataItem": ".history_data_item",
    "HistoryDataItemEvent": ".history_data_item_event",
    "HistoryFilters": ".history_filters",
    "HistoryOrder": ".history_order",
    "HistoryOrderOrder": ".history_order_order",
    "HistoryPagination": ".history_pagination",
    "List": ".list_",
    "ListEnvelope": ".list_envelope",
    "ListList": ".list_list",
    "ListState": ".list_state",
    "Member": ".member",
    "MemberEnvelope": ".member_envelope",
    "MemberList": ".member_list",
    "MemberState": ".member_state",
    "Report": ".report",
    "ReportEnvelope": ".report_envelope",
    "ReportList": ".report_list",
    "Segment": ".segment",
    "SegmentEnvelope": ".segment_envelope",
    "SegmentList": ".segment_list",
    "SegmentState": ".segment_state",
    "SyncResult": ".sync_result",
    "SyncResultReport": ".sync_result_report",
    "Webhook": ".webhook",
    "WebhookEnvelope": ".webhook_envelope",
    "WebhookEvent": ".webhook_event",
    "WebhookList": ".webhook_list",
    "WebhookState": ".webhook_state",
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
    "Campaign",
    "CampaignContent",
    "CampaignContentCampaign",
    "CampaignContentCampaignReport",
    "CampaignEnvelope",
    "CampaignList",
    "Error",
    "ErrorError",
    "ErrorErrorType",
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
    "Report",
    "ReportEnvelope",
    "ReportList",
    "Segment",
    "SegmentEnvelope",
    "SegmentList",
    "SegmentState",
    "SyncResult",
    "SyncResultReport",
    "Webhook",
    "WebhookEnvelope",
    "WebhookEvent",
    "WebhookList",
    "WebhookState",
]
