



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v1query_workflows_response import PostV1QueryWorkflowsResponse
    from .post_v1workflows_request_tasks_item import PostV1WorkflowsRequestTasksItem
    from .post_v1workflows_request_tasks_item_pilot_config import PostV1WorkflowsRequestTasksItemPilotConfig
    from .post_v1workflows_request_tasks_item_pilot_config_environment_value import (
        PostV1WorkflowsRequestTasksItemPilotConfigEnvironmentValue,
    )
    from .post_v1workflows_request_tasks_item_pilot_config_image_source import (
        PostV1WorkflowsRequestTasksItemPilotConfigImageSource,
    )
    from .post_v1workflows_request_tasks_item_worker_config import PostV1WorkflowsRequestTasksItemWorkerConfig
    from .post_v1workflows_request_tasks_item_worker_config_worker_disk import (
        PostV1WorkflowsRequestTasksItemWorkerConfigWorkerDisk,
    )
    from .post_v1workflows_request_tasks_item_worker_config_worker_memory import (
        PostV1WorkflowsRequestTasksItemWorkerConfigWorkerMemory,
    )
    from .post_v1workflows_response import PostV1WorkflowsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "PostV1QueryWorkflowsResponse": ".post_v1query_workflows_response",
    "PostV1WorkflowsRequestTasksItem": ".post_v1workflows_request_tasks_item",
    "PostV1WorkflowsRequestTasksItemPilotConfig": ".post_v1workflows_request_tasks_item_pilot_config",
    "PostV1WorkflowsRequestTasksItemPilotConfigEnvironmentValue": ".post_v1workflows_request_tasks_item_pilot_config_environment_value",
    "PostV1WorkflowsRequestTasksItemPilotConfigImageSource": ".post_v1workflows_request_tasks_item_pilot_config_image_source",
    "PostV1WorkflowsRequestTasksItemWorkerConfig": ".post_v1workflows_request_tasks_item_worker_config",
    "PostV1WorkflowsRequestTasksItemWorkerConfigWorkerDisk": ".post_v1workflows_request_tasks_item_worker_config_worker_disk",
    "PostV1WorkflowsRequestTasksItemWorkerConfigWorkerMemory": ".post_v1workflows_request_tasks_item_worker_config_worker_memory",
    "PostV1WorkflowsResponse": ".post_v1workflows_response",
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
    "PostV1QueryWorkflowsResponse",
    "PostV1WorkflowsRequestTasksItem",
    "PostV1WorkflowsRequestTasksItemPilotConfig",
    "PostV1WorkflowsRequestTasksItemPilotConfigEnvironmentValue",
    "PostV1WorkflowsRequestTasksItemPilotConfigImageSource",
    "PostV1WorkflowsRequestTasksItemWorkerConfig",
    "PostV1WorkflowsRequestTasksItemWorkerConfigWorkerDisk",
    "PostV1WorkflowsRequestTasksItemWorkerConfigWorkerMemory",
    "PostV1WorkflowsResponse",
]
