



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action import Action
    from .action_collection import ActionCollection
    from .action_resource import ActionResource
    from .basic_dag_run import BasicDagRun
    from .class_reference import ClassReference
    from .collection_info import CollectionInfo
    from .color import Color
    from .config import Config
    from .config_option import ConfigOption
    from .config_section import ConfigSection
    from .connection import Connection
    from .connection_collection import ConnectionCollection
    from .connection_collection_item import ConnectionCollectionItem
    from .connection_test import ConnectionTest
    from .cron_expression import CronExpression
    from .dag import Dag
    from .dag_collection import DagCollection
    from .dag_detail import DagDetail
    from .dag_run import DagRun
    from .dag_run_collection import DagRunCollection
    from .dag_run_run_type import DagRunRunType
    from .dag_schedule_dataset_reference import DagScheduleDatasetReference
    from .dag_state import DagState
    from .dag_warning import DagWarning
    from .dag_warning_collection import DagWarningCollection
    from .dataset import Dataset
    from .dataset_collection import DatasetCollection
    from .dataset_event import DatasetEvent
    from .dataset_event_collection import DatasetEventCollection
    from .error import Error
    from .event_log import EventLog
    from .event_log_collection import EventLogCollection
    from .extra_link import ExtraLink
    from .extra_link_collection import ExtraLinkCollection
    from .health_info import HealthInfo
    from .health_status import HealthStatus
    from .import_error import ImportError
    from .import_error_collection import ImportErrorCollection
    from .job import Job
    from .metadatabase_status import MetadatabaseStatus
    from .plugin_collection import PluginCollection
    from .plugin_collection_item import PluginCollectionItem
    from .pool import Pool
    from .pool_collection import PoolCollection
    from .provider import Provider
    from .provider_collection import ProviderCollection
    from .relative_delta import RelativeDelta
    from .resource import Resource
    from .role import Role
    from .role_collection import RoleCollection
    from .schedule_interval import ScheduleInterval
    from .scheduler_status import SchedulerStatus
    from .set_task_instance_note import SetTaskInstanceNote
    from .sla_miss import SlaMiss
    from .tag import Tag
    from .task import Task
    from .task_collection import TaskCollection
    from .task_extra_links_item import TaskExtraLinksItem
    from .task_instance import TaskInstance
    from .task_instance_collection import TaskInstanceCollection
    from .task_instance_reference import TaskInstanceReference
    from .task_instance_reference_collection import TaskInstanceReferenceCollection
    from .task_outlet_dataset_reference import TaskOutletDatasetReference
    from .task_state import TaskState
    from .time_delta import TimeDelta
    from .timezone import Timezone
    from .trigger import Trigger
    from .trigger_rule import TriggerRule
    from .update_task_instance import UpdateTaskInstance
    from .update_task_instance_new_state import UpdateTaskInstanceNewState
    from .user import User
    from .user_collection import UserCollection
    from .user_collection_item import UserCollectionItem
    from .user_collection_item_roles_item import UserCollectionItemRolesItem
    from .variable import Variable
    from .variable_collection import VariableCollection
    from .variable_collection_item import VariableCollectionItem
    from .version_info import VersionInfo
    from .weight_rule import WeightRule
    from .x_com import XCom
    from .x_com_collection import XComCollection
    from .x_com_collection_item import XComCollectionItem
_dynamic_imports: typing.Dict[str, str] = {
    "Action": ".action",
    "ActionCollection": ".action_collection",
    "ActionResource": ".action_resource",
    "BasicDagRun": ".basic_dag_run",
    "ClassReference": ".class_reference",
    "CollectionInfo": ".collection_info",
    "Color": ".color",
    "Config": ".config",
    "ConfigOption": ".config_option",
    "ConfigSection": ".config_section",
    "Connection": ".connection",
    "ConnectionCollection": ".connection_collection",
    "ConnectionCollectionItem": ".connection_collection_item",
    "ConnectionTest": ".connection_test",
    "CronExpression": ".cron_expression",
    "Dag": ".dag",
    "DagCollection": ".dag_collection",
    "DagDetail": ".dag_detail",
    "DagRun": ".dag_run",
    "DagRunCollection": ".dag_run_collection",
    "DagRunRunType": ".dag_run_run_type",
    "DagScheduleDatasetReference": ".dag_schedule_dataset_reference",
    "DagState": ".dag_state",
    "DagWarning": ".dag_warning",
    "DagWarningCollection": ".dag_warning_collection",
    "Dataset": ".dataset",
    "DatasetCollection": ".dataset_collection",
    "DatasetEvent": ".dataset_event",
    "DatasetEventCollection": ".dataset_event_collection",
    "Error": ".error",
    "EventLog": ".event_log",
    "EventLogCollection": ".event_log_collection",
    "ExtraLink": ".extra_link",
    "ExtraLinkCollection": ".extra_link_collection",
    "HealthInfo": ".health_info",
    "HealthStatus": ".health_status",
    "ImportError": ".import_error",
    "ImportErrorCollection": ".import_error_collection",
    "Job": ".job",
    "MetadatabaseStatus": ".metadatabase_status",
    "PluginCollection": ".plugin_collection",
    "PluginCollectionItem": ".plugin_collection_item",
    "Pool": ".pool",
    "PoolCollection": ".pool_collection",
    "Provider": ".provider",
    "ProviderCollection": ".provider_collection",
    "RelativeDelta": ".relative_delta",
    "Resource": ".resource",
    "Role": ".role",
    "RoleCollection": ".role_collection",
    "ScheduleInterval": ".schedule_interval",
    "SchedulerStatus": ".scheduler_status",
    "SetTaskInstanceNote": ".set_task_instance_note",
    "SlaMiss": ".sla_miss",
    "Tag": ".tag",
    "Task": ".task",
    "TaskCollection": ".task_collection",
    "TaskExtraLinksItem": ".task_extra_links_item",
    "TaskInstance": ".task_instance",
    "TaskInstanceCollection": ".task_instance_collection",
    "TaskInstanceReference": ".task_instance_reference",
    "TaskInstanceReferenceCollection": ".task_instance_reference_collection",
    "TaskOutletDatasetReference": ".task_outlet_dataset_reference",
    "TaskState": ".task_state",
    "TimeDelta": ".time_delta",
    "Timezone": ".timezone",
    "Trigger": ".trigger",
    "TriggerRule": ".trigger_rule",
    "UpdateTaskInstance": ".update_task_instance",
    "UpdateTaskInstanceNewState": ".update_task_instance_new_state",
    "User": ".user",
    "UserCollection": ".user_collection",
    "UserCollectionItem": ".user_collection_item",
    "UserCollectionItemRolesItem": ".user_collection_item_roles_item",
    "Variable": ".variable",
    "VariableCollection": ".variable_collection",
    "VariableCollectionItem": ".variable_collection_item",
    "VersionInfo": ".version_info",
    "WeightRule": ".weight_rule",
    "XCom": ".x_com",
    "XComCollection": ".x_com_collection",
    "XComCollectionItem": ".x_com_collection_item",
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
    "Action",
    "ActionCollection",
    "ActionResource",
    "BasicDagRun",
    "ClassReference",
    "CollectionInfo",
    "Color",
    "Config",
    "ConfigOption",
    "ConfigSection",
    "Connection",
    "ConnectionCollection",
    "ConnectionCollectionItem",
    "ConnectionTest",
    "CronExpression",
    "Dag",
    "DagCollection",
    "DagDetail",
    "DagRun",
    "DagRunCollection",
    "DagRunRunType",
    "DagScheduleDatasetReference",
    "DagState",
    "DagWarning",
    "DagWarningCollection",
    "Dataset",
    "DatasetCollection",
    "DatasetEvent",
    "DatasetEventCollection",
    "Error",
    "EventLog",
    "EventLogCollection",
    "ExtraLink",
    "ExtraLinkCollection",
    "HealthInfo",
    "HealthStatus",
    "ImportError",
    "ImportErrorCollection",
    "Job",
    "MetadatabaseStatus",
    "PluginCollection",
    "PluginCollectionItem",
    "Pool",
    "PoolCollection",
    "Provider",
    "ProviderCollection",
    "RelativeDelta",
    "Resource",
    "Role",
    "RoleCollection",
    "ScheduleInterval",
    "SchedulerStatus",
    "SetTaskInstanceNote",
    "SlaMiss",
    "Tag",
    "Task",
    "TaskCollection",
    "TaskExtraLinksItem",
    "TaskInstance",
    "TaskInstanceCollection",
    "TaskInstanceReference",
    "TaskInstanceReferenceCollection",
    "TaskOutletDatasetReference",
    "TaskState",
    "TimeDelta",
    "Timezone",
    "Trigger",
    "TriggerRule",
    "UpdateTaskInstance",
    "UpdateTaskInstanceNewState",
    "User",
    "UserCollection",
    "UserCollectionItem",
    "UserCollectionItemRolesItem",
    "Variable",
    "VariableCollection",
    "VariableCollectionItem",
    "VersionInfo",
    "WeightRule",
    "XCom",
    "XComCollection",
    "XComCollectionItem",
]
