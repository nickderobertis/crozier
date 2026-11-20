



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        ColumnEdge,
        ColumnGraph,
        ColumnNeighbors,
        ColumnNode,
        ColumnRef,
        Creator,
        DatasetGovernance,
        DatasetRef,
        DatasetSchema,
        DatasetSummary,
        Datasets,
        DemoDataset,
        DemoDatasets,
        DemoField,
        DemoVersion,
        DlqBacklog,
        DlqEvent,
        DlqReplayResponse,
        EstateGraph,
        EventRecord,
        Events,
        GraphEdge,
        GraphNode,
        HttpValidationError,
        JobSummary,
        Jobs,
        LineageGraph,
        Liveness,
        LivenessStatus,
        Namespaces,
        Neighbors,
        ProducerInfo,
        Producers,
        ReaderInfo,
        Readers,
        Readiness,
        ReadinessStatus,
        ReconcileState,
        ReconcileStatus,
        RunInput,
        RunInputs,
        RunStatus,
        Runs,
        SchemaField,
        SearchHit,
        SearchResults,
        ValidationError,
        ValidationErrorLocItem,
    )
    from .errors import UnprocessableEntityError
    from . import admin, demo, discovery, governance, health, ingest, pub_sub, query
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "ColumnEdge": ".types",
    "ColumnGraph": ".types",
    "ColumnNeighbors": ".types",
    "ColumnNode": ".types",
    "ColumnRef": ".types",
    "Creator": ".types",
    "DatasetGovernance": ".types",
    "DatasetRef": ".types",
    "DatasetSchema": ".types",
    "DatasetSummary": ".types",
    "Datasets": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "DemoDataset": ".types",
    "DemoDatasets": ".types",
    "DemoField": ".types",
    "DemoVersion": ".types",
    "DlqBacklog": ".types",
    "DlqEvent": ".types",
    "DlqReplayResponse": ".types",
    "EstateGraph": ".types",
    "EventRecord": ".types",
    "Events": ".types",
    "FernApi": ".client",
    "GraphEdge": ".types",
    "GraphNode": ".types",
    "HttpValidationError": ".types",
    "JobSummary": ".types",
    "Jobs": ".types",
    "LineageGraph": ".types",
    "Liveness": ".types",
    "LivenessStatus": ".types",
    "Namespaces": ".types",
    "Neighbors": ".types",
    "ProducerInfo": ".types",
    "Producers": ".types",
    "ReaderInfo": ".types",
    "Readers": ".types",
    "Readiness": ".types",
    "ReadinessStatus": ".types",
    "ReconcileState": ".types",
    "ReconcileStatus": ".types",
    "RunInput": ".types",
    "RunInputs": ".types",
    "RunStatus": ".types",
    "Runs": ".types",
    "SchemaField": ".types",
    "SearchHit": ".types",
    "SearchResults": ".types",
    "UnprocessableEntityError": ".errors",
    "ValidationError": ".types",
    "ValidationErrorLocItem": ".types",
    "__version__": ".version",
    "admin": ".admin",
    "demo": ".demo",
    "discovery": ".discovery",
    "governance": ".governance",
    "health": ".health",
    "ingest": ".ingest",
    "pub_sub": ".pub_sub",
    "query": ".query",
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
    "ColumnEdge",
    "ColumnGraph",
    "ColumnNeighbors",
    "ColumnNode",
    "ColumnRef",
    "Creator",
    "DatasetGovernance",
    "DatasetRef",
    "DatasetSchema",
    "DatasetSummary",
    "Datasets",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "DemoDataset",
    "DemoDatasets",
    "DemoField",
    "DemoVersion",
    "DlqBacklog",
    "DlqEvent",
    "DlqReplayResponse",
    "EstateGraph",
    "EventRecord",
    "Events",
    "FernApi",
    "GraphEdge",
    "GraphNode",
    "HttpValidationError",
    "JobSummary",
    "Jobs",
    "LineageGraph",
    "Liveness",
    "LivenessStatus",
    "Namespaces",
    "Neighbors",
    "ProducerInfo",
    "Producers",
    "ReaderInfo",
    "Readers",
    "Readiness",
    "ReadinessStatus",
    "ReconcileState",
    "ReconcileStatus",
    "RunInput",
    "RunInputs",
    "RunStatus",
    "Runs",
    "SchemaField",
    "SearchHit",
    "SearchResults",
    "UnprocessableEntityError",
    "ValidationError",
    "ValidationErrorLocItem",
    "__version__",
    "admin",
    "demo",
    "discovery",
    "governance",
    "health",
    "ingest",
    "pub_sub",
    "query",
]
