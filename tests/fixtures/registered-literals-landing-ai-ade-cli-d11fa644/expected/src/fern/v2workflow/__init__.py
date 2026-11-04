



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        V2WorkflowCreateJobRequestServiceTier,
        V2WorkflowCreateJobResponse,
        V2WorkflowCreateJobResponseStatus,
        V2WorkflowGetJobResponse,
        V2WorkflowGetJobResponseError,
        V2WorkflowGetJobResponseResult,
        V2WorkflowGetJobResponseStatus,
        V2WorkflowListJobsResponse,
        V2WorkflowListJobsResponseJobsItem,
        V2WorkflowListJobsResponseJobsItemStatus,
        V2WorkflowRunSyncResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "V2WorkflowCreateJobRequestServiceTier": ".types",
    "V2WorkflowCreateJobResponse": ".types",
    "V2WorkflowCreateJobResponseStatus": ".types",
    "V2WorkflowGetJobResponse": ".types",
    "V2WorkflowGetJobResponseError": ".types",
    "V2WorkflowGetJobResponseResult": ".types",
    "V2WorkflowGetJobResponseStatus": ".types",
    "V2WorkflowListJobsResponse": ".types",
    "V2WorkflowListJobsResponseJobsItem": ".types",
    "V2WorkflowListJobsResponseJobsItemStatus": ".types",
    "V2WorkflowRunSyncResponse": ".types",
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
    "V2WorkflowCreateJobRequestServiceTier",
    "V2WorkflowCreateJobResponse",
    "V2WorkflowCreateJobResponseStatus",
    "V2WorkflowGetJobResponse",
    "V2WorkflowGetJobResponseError",
    "V2WorkflowGetJobResponseResult",
    "V2WorkflowGetJobResponseStatus",
    "V2WorkflowListJobsResponse",
    "V2WorkflowListJobsResponseJobsItem",
    "V2WorkflowListJobsResponseJobsItemStatus",
    "V2WorkflowRunSyncResponse",
]
