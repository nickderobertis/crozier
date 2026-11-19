



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .column_edge import ColumnEdge
    from .column_graph import ColumnGraph
    from .column_neighbors import ColumnNeighbors
    from .column_node import ColumnNode
    from .column_ref import ColumnRef
    from .creator import Creator
    from .dataset_governance import DatasetGovernance
    from .dataset_ref import DatasetRef
    from .dataset_schema import DatasetSchema
    from .dataset_summary import DatasetSummary
    from .datasets import Datasets
    from .demo_dataset import DemoDataset
    from .demo_datasets import DemoDatasets
    from .demo_field import DemoField
    from .demo_version import DemoVersion
    from .dlq_backlog import DlqBacklog
    from .dlq_event import DlqEvent
    from .dlq_replay_response import DlqReplayResponse
    from .estate_graph import EstateGraph
    from .event_record import EventRecord
    from .events import Events
    from .graph_edge import GraphEdge
    from .graph_node import GraphNode
    from .http_validation_error import HttpValidationError
    from .job_summary import JobSummary
    from .jobs import Jobs
    from .lineage_graph import LineageGraph
    from .liveness import Liveness
    from .liveness_status import LivenessStatus
    from .namespaces import Namespaces
    from .neighbors import Neighbors
    from .producer_info import ProducerInfo
    from .producers import Producers
    from .reader_info import ReaderInfo
    from .readers import Readers
    from .readiness import Readiness
    from .readiness_status import ReadinessStatus
    from .reconcile_state import ReconcileState
    from .reconcile_status import ReconcileStatus
    from .run_input import RunInput
    from .run_inputs import RunInputs
    from .run_status import RunStatus
    from .runs import Runs
    from .schema_field import SchemaField
    from .search_hit import SearchHit
    from .search_results import SearchResults
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "ColumnEdge": ".column_edge",
    "ColumnGraph": ".column_graph",
    "ColumnNeighbors": ".column_neighbors",
    "ColumnNode": ".column_node",
    "ColumnRef": ".column_ref",
    "Creator": ".creator",
    "DatasetGovernance": ".dataset_governance",
    "DatasetRef": ".dataset_ref",
    "DatasetSchema": ".dataset_schema",
    "DatasetSummary": ".dataset_summary",
    "Datasets": ".datasets",
    "DemoDataset": ".demo_dataset",
    "DemoDatasets": ".demo_datasets",
    "DemoField": ".demo_field",
    "DemoVersion": ".demo_version",
    "DlqBacklog": ".dlq_backlog",
    "DlqEvent": ".dlq_event",
    "DlqReplayResponse": ".dlq_replay_response",
    "EstateGraph": ".estate_graph",
    "EventRecord": ".event_record",
    "Events": ".events",
    "GraphEdge": ".graph_edge",
    "GraphNode": ".graph_node",
    "HttpValidationError": ".http_validation_error",
    "JobSummary": ".job_summary",
    "Jobs": ".jobs",
    "LineageGraph": ".lineage_graph",
    "Liveness": ".liveness",
    "LivenessStatus": ".liveness_status",
    "Namespaces": ".namespaces",
    "Neighbors": ".neighbors",
    "ProducerInfo": ".producer_info",
    "Producers": ".producers",
    "ReaderInfo": ".reader_info",
    "Readers": ".readers",
    "Readiness": ".readiness",
    "ReadinessStatus": ".readiness_status",
    "ReconcileState": ".reconcile_state",
    "ReconcileStatus": ".reconcile_status",
    "RunInput": ".run_input",
    "RunInputs": ".run_inputs",
    "RunStatus": ".run_status",
    "Runs": ".runs",
    "SchemaField": ".schema_field",
    "SearchHit": ".search_hit",
    "SearchResults": ".search_results",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "ValidationError",
    "ValidationErrorLocItem",
]
