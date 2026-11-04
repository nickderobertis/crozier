



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ActiveAlertResponse,
        AlertEventResponse,
        AlertRuleRequest,
        AlertRuleResponse,
        AlertStateValue,
        AlertStatusResponse,
        CatalogNode,
        ChannelSummary,
        ChannelType,
        CollectionNode,
        ConnectionRequest,
        ConnectionResponse,
        DestinationRequest,
        DestinationResponse,
        Duration,
        Instant,
        Metadata,
        NamedRef,
        NotificationChannelRequest,
        NotificationChannelResponse,
        Operator,
        PagedAlertEventResponse,
        PanelQueryResponse,
        PanelResponse,
        PanelsListResponse,
        PipelineResponse,
        PipelineStatus,
        PredicateDto,
        ReduceFunction,
        SchemaNode,
        Severity,
        Signal,
        SignalResponse,
        SourceRequest,
        SourceResponse,
        TimeRange,
        TimeSeries,
        TransformRequest,
        TransformResponse,
        Type,
        VaultRequest,
        VaultResponse,
        Visualization,
    )
    from .errors import BadRequestError, NotFoundError
    from . import (
        alerting,
        catalog_resource,
        connections,
        destinations,
        monitoring,
        pipelines,
        sources,
        transforms,
        vaults,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .connections import GetApiConnectionsIdCollectionsResponse, PostApiConnectionsValidateResponse
    from .environment import FernApiEnvironment
    from .sources import PostApiSourcesSignalsVerifyResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "ActiveAlertResponse": ".types",
    "AlertEventResponse": ".types",
    "AlertRuleRequest": ".types",
    "AlertRuleResponse": ".types",
    "AlertStateValue": ".types",
    "AlertStatusResponse": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CatalogNode": ".types",
    "ChannelSummary": ".types",
    "ChannelType": ".types",
    "CollectionNode": ".types",
    "ConnectionRequest": ".types",
    "ConnectionResponse": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DestinationRequest": ".types",
    "DestinationResponse": ".types",
    "Duration": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetApiConnectionsIdCollectionsResponse": ".connections",
    "Instant": ".types",
    "Metadata": ".types",
    "NamedRef": ".types",
    "NotFoundError": ".errors",
    "NotificationChannelRequest": ".types",
    "NotificationChannelResponse": ".types",
    "Operator": ".types",
    "PagedAlertEventResponse": ".types",
    "PanelQueryResponse": ".types",
    "PanelResponse": ".types",
    "PanelsListResponse": ".types",
    "PipelineResponse": ".types",
    "PipelineStatus": ".types",
    "PostApiConnectionsValidateResponse": ".connections",
    "PostApiSourcesSignalsVerifyResponse": ".sources",
    "PredicateDto": ".types",
    "ReduceFunction": ".types",
    "SchemaNode": ".types",
    "Severity": ".types",
    "Signal": ".types",
    "SignalResponse": ".types",
    "SourceRequest": ".types",
    "SourceResponse": ".types",
    "TimeRange": ".types",
    "TimeSeries": ".types",
    "TransformRequest": ".types",
    "TransformResponse": ".types",
    "Type": ".types",
    "VaultRequest": ".types",
    "VaultResponse": ".types",
    "Visualization": ".types",
    "__version__": ".version",
    "alerting": ".alerting",
    "catalog_resource": ".catalog_resource",
    "connections": ".connections",
    "destinations": ".destinations",
    "monitoring": ".monitoring",
    "pipelines": ".pipelines",
    "sources": ".sources",
    "transforms": ".transforms",
    "vaults": ".vaults",
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
    "AsyncFernApi",
    "BadRequestError",
    "CatalogNode",
    "ChannelSummary",
    "ChannelType",
    "CollectionNode",
    "ConnectionRequest",
    "ConnectionResponse",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DestinationRequest",
    "DestinationResponse",
    "Duration",
    "FernApi",
    "FernApiEnvironment",
    "GetApiConnectionsIdCollectionsResponse",
    "Instant",
    "Metadata",
    "NamedRef",
    "NotFoundError",
    "NotificationChannelRequest",
    "NotificationChannelResponse",
    "Operator",
    "PagedAlertEventResponse",
    "PanelQueryResponse",
    "PanelResponse",
    "PanelsListResponse",
    "PipelineResponse",
    "PipelineStatus",
    "PostApiConnectionsValidateResponse",
    "PostApiSourcesSignalsVerifyResponse",
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
    "__version__",
    "alerting",
    "catalog_resource",
    "connections",
    "destinations",
    "monitoring",
    "pipelines",
    "sources",
    "transforms",
    "vaults",
]
