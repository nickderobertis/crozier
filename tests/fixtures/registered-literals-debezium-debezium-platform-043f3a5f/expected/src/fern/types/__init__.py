



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .active_alert_response import ActiveAlertResponse
    from .alert_event_response import AlertEventResponse
    from .alert_rule_request import AlertRuleRequest
    from .alert_rule_response import AlertRuleResponse
    from .alert_state_value import AlertStateValue
    from .alert_status_response import AlertStatusResponse
    from .catalog_node import CatalogNode
    from .channel_summary import ChannelSummary
    from .channel_type import ChannelType
    from .collection_node import CollectionNode
    from .connection_request import ConnectionRequest
    from .connection_response import ConnectionResponse
    from .destination_request import DestinationRequest
    from .destination_response import DestinationResponse
    from .duration import Duration
    from .instant import Instant
    from .metadata import Metadata
    from .named_ref import NamedRef
    from .notification_channel_request import NotificationChannelRequest
    from .notification_channel_response import NotificationChannelResponse
    from .operator import Operator
    from .paged_alert_event_response import PagedAlertEventResponse
    from .panel_query_response import PanelQueryResponse
    from .panel_response import PanelResponse
    from .panels_list_response import PanelsListResponse
    from .pipeline_response import PipelineResponse
    from .pipeline_status import PipelineStatus
    from .predicate_dto import PredicateDto
    from .reduce_function import ReduceFunction
    from .schema_node import SchemaNode
    from .severity import Severity
    from .signal import Signal
    from .signal_response import SignalResponse
    from .source_request import SourceRequest
    from .source_response import SourceResponse
    from .time_range import TimeRange
    from .time_series import TimeSeries
    from .transform_request import TransformRequest
    from .transform_response import TransformResponse
    from .type import Type
    from .vault_request import VaultRequest
    from .vault_response import VaultResponse
    from .visualization import Visualization
_dynamic_imports: typing.Dict[str, str] = {
    "ActiveAlertResponse": ".active_alert_response",
    "AlertEventResponse": ".alert_event_response",
    "AlertRuleRequest": ".alert_rule_request",
    "AlertRuleResponse": ".alert_rule_response",
    "AlertStateValue": ".alert_state_value",
    "AlertStatusResponse": ".alert_status_response",
    "CatalogNode": ".catalog_node",
    "ChannelSummary": ".channel_summary",
    "ChannelType": ".channel_type",
    "CollectionNode": ".collection_node",
    "ConnectionRequest": ".connection_request",
    "ConnectionResponse": ".connection_response",
    "DestinationRequest": ".destination_request",
    "DestinationResponse": ".destination_response",
    "Duration": ".duration",
    "Instant": ".instant",
    "Metadata": ".metadata",
    "NamedRef": ".named_ref",
    "NotificationChannelRequest": ".notification_channel_request",
    "NotificationChannelResponse": ".notification_channel_response",
    "Operator": ".operator",
    "PagedAlertEventResponse": ".paged_alert_event_response",
    "PanelQueryResponse": ".panel_query_response",
    "PanelResponse": ".panel_response",
    "PanelsListResponse": ".panels_list_response",
    "PipelineResponse": ".pipeline_response",
    "PipelineStatus": ".pipeline_status",
    "PredicateDto": ".predicate_dto",
    "ReduceFunction": ".reduce_function",
    "SchemaNode": ".schema_node",
    "Severity": ".severity",
    "Signal": ".signal",
    "SignalResponse": ".signal_response",
    "SourceRequest": ".source_request",
    "SourceResponse": ".source_response",
    "TimeRange": ".time_range",
    "TimeSeries": ".time_series",
    "TransformRequest": ".transform_request",
    "TransformResponse": ".transform_response",
    "Type": ".type",
    "VaultRequest": ".vault_request",
    "VaultResponse": ".vault_response",
    "Visualization": ".visualization",
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
    "ActiveAlertResponse",
    "AlertEventResponse",
    "AlertRuleRequest",
    "AlertRuleResponse",
    "AlertStateValue",
    "AlertStatusResponse",
    "CatalogNode",
    "ChannelSummary",
    "ChannelType",
    "CollectionNode",
    "ConnectionRequest",
    "ConnectionResponse",
    "DestinationRequest",
    "DestinationResponse",
    "Duration",
    "Instant",
    "Metadata",
    "NamedRef",
    "NotificationChannelRequest",
    "NotificationChannelResponse",
    "Operator",
    "PagedAlertEventResponse",
    "PanelQueryResponse",
    "PanelResponse",
    "PanelsListResponse",
    "PipelineResponse",
    "PipelineStatus",
    "PredicateDto",
    "ReduceFunction",
    "SchemaNode",
    "Severity",
    "Signal",
    "SignalResponse",
    "SourceRequest",
    "SourceResponse",
    "TimeRange",
    "TimeSeries",
    "TransformRequest",
    "TransformResponse",
    "Type",
    "VaultRequest",
    "VaultResponse",
    "Visualization",
]
