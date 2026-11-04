



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .deactivated_workflow_response_object import DeactivatedWorkflowResponseObject
    from .error_response import ErrorResponse
    from .find_object import FindObject
    from .query_next_after import QueryNextAfter
    from .task_directive_object import TaskDirectiveObject
    from .taskforce_object import TaskforceObject
    from .taskforce_object_phase import TaskforceObjectPhase
    from .taskforce_object_phase_change_log_item import TaskforceObjectPhaseChangeLogItem
    from .taskforce_object_pilot_config import TaskforceObjectPilotConfig
    from .taskforce_object_pilot_config_environment_value import TaskforceObjectPilotConfigEnvironmentValue
    from .taskforce_object_pilot_config_image_source import TaskforceObjectPilotConfigImageSource
    from .taskforce_object_submit_dict_value import TaskforceObjectSubmitDictValue
    from .taskforce_object_worker_config import TaskforceObjectWorkerConfig
    from .taskforce_object_worker_config_worker_disk import TaskforceObjectWorkerConfigWorkerDisk
    from .taskforce_object_worker_config_worker_memory import TaskforceObjectWorkerConfigWorkerMemory
    from .workflow_object import WorkflowObject
    from .workflow_object_deactivated import WorkflowObjectDeactivated
_dynamic_imports: typing.Dict[str, str] = {
    "DeactivatedWorkflowResponseObject": ".deactivated_workflow_response_object",
    "ErrorResponse": ".error_response",
    "FindObject": ".find_object",
    "QueryNextAfter": ".query_next_after",
    "TaskDirectiveObject": ".task_directive_object",
    "TaskforceObject": ".taskforce_object",
    "TaskforceObjectPhase": ".taskforce_object_phase",
    "TaskforceObjectPhaseChangeLogItem": ".taskforce_object_phase_change_log_item",
    "TaskforceObjectPilotConfig": ".taskforce_object_pilot_config",
    "TaskforceObjectPilotConfigEnvironmentValue": ".taskforce_object_pilot_config_environment_value",
    "TaskforceObjectPilotConfigImageSource": ".taskforce_object_pilot_config_image_source",
    "TaskforceObjectSubmitDictValue": ".taskforce_object_submit_dict_value",
    "TaskforceObjectWorkerConfig": ".taskforce_object_worker_config",
    "TaskforceObjectWorkerConfigWorkerDisk": ".taskforce_object_worker_config_worker_disk",
    "TaskforceObjectWorkerConfigWorkerMemory": ".taskforce_object_worker_config_worker_memory",
    "WorkflowObject": ".workflow_object",
    "WorkflowObjectDeactivated": ".workflow_object_deactivated",
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
    "DeactivatedWorkflowResponseObject",
    "ErrorResponse",
    "FindObject",
    "QueryNextAfter",
    "TaskDirectiveObject",
    "TaskforceObject",
    "TaskforceObjectPhase",
    "TaskforceObjectPhaseChangeLogItem",
    "TaskforceObjectPilotConfig",
    "TaskforceObjectPilotConfigEnvironmentValue",
    "TaskforceObjectPilotConfigImageSource",
    "TaskforceObjectSubmitDictValue",
    "TaskforceObjectWorkerConfig",
    "TaskforceObjectWorkerConfigWorkerDisk",
    "TaskforceObjectWorkerConfigWorkerMemory",
    "WorkflowObject",
    "WorkflowObjectDeactivated",
]
