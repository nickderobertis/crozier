



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .check_availability_task import CheckAvailabilityTask
    from .collection_links import CollectionLinks
    from .collection_metadata import CollectionMetadata
    from .error_not_found import ErrorNotFound
    from .error_not_found_errors_item import ErrorNotFoundErrorsItem
    from .full_refresh_persister_task import FullRefreshPersisterTask
    from .full_refresh_upload_task import FullRefreshUploadTask
    from .graph_ql_response import GraphQlResponse
    from .id import Id
    from .incremental_refresh_upload_task import IncrementalRefreshUploadTask
    from .launch_job_task import LaunchJobTask
    from .order_parameters_service_plan import OrderParametersServicePlan
    from .service_credential import ServiceCredential
    from .service_credential_type import ServiceCredentialType
    from .service_credential_types_collection import ServiceCredentialTypesCollection
    from .service_credentials_collection import ServiceCredentialsCollection
    from .service_instance import ServiceInstance
    from .service_instance_node import ServiceInstanceNode
    from .service_instance_nodes_collection import ServiceInstanceNodesCollection
    from .service_instances_collection import ServiceInstancesCollection
    from .service_inventories_collection import ServiceInventoriesCollection
    from .service_inventory import ServiceInventory
    from .service_offering import ServiceOffering
    from .service_offering_icon import ServiceOfferingIcon
    from .service_offering_icons_collection import ServiceOfferingIconsCollection
    from .service_offering_node import ServiceOfferingNode
    from .service_offering_nodes_collection import ServiceOfferingNodesCollection
    from .service_offerings_collection import ServiceOfferingsCollection
    from .service_plan import ServicePlan
    from .service_plans_collection import ServicePlansCollection
    from .source import Source
    from .sources_collection import SourcesCollection
    from .tag import Tag
    from .tags_collection import TagsCollection
    from .task import Task
    from .task_state import TaskState
    from .task_status import TaskStatus
    from .tasks_collection import TasksCollection
    from .tenant import Tenant
    from .towing_task import TowingTask
    from .uuid_ import Uuid
_dynamic_imports: typing.Dict[str, str] = {
    "CheckAvailabilityTask": ".check_availability_task",
    "CollectionLinks": ".collection_links",
    "CollectionMetadata": ".collection_metadata",
    "ErrorNotFound": ".error_not_found",
    "ErrorNotFoundErrorsItem": ".error_not_found_errors_item",
    "FullRefreshPersisterTask": ".full_refresh_persister_task",
    "FullRefreshUploadTask": ".full_refresh_upload_task",
    "GraphQlResponse": ".graph_ql_response",
    "Id": ".id",
    "IncrementalRefreshUploadTask": ".incremental_refresh_upload_task",
    "LaunchJobTask": ".launch_job_task",
    "OrderParametersServicePlan": ".order_parameters_service_plan",
    "ServiceCredential": ".service_credential",
    "ServiceCredentialType": ".service_credential_type",
    "ServiceCredentialTypesCollection": ".service_credential_types_collection",
    "ServiceCredentialsCollection": ".service_credentials_collection",
    "ServiceInstance": ".service_instance",
    "ServiceInstanceNode": ".service_instance_node",
    "ServiceInstanceNodesCollection": ".service_instance_nodes_collection",
    "ServiceInstancesCollection": ".service_instances_collection",
    "ServiceInventoriesCollection": ".service_inventories_collection",
    "ServiceInventory": ".service_inventory",
    "ServiceOffering": ".service_offering",
    "ServiceOfferingIcon": ".service_offering_icon",
    "ServiceOfferingIconsCollection": ".service_offering_icons_collection",
    "ServiceOfferingNode": ".service_offering_node",
    "ServiceOfferingNodesCollection": ".service_offering_nodes_collection",
    "ServiceOfferingsCollection": ".service_offerings_collection",
    "ServicePlan": ".service_plan",
    "ServicePlansCollection": ".service_plans_collection",
    "Source": ".source",
    "SourcesCollection": ".sources_collection",
    "Tag": ".tag",
    "TagsCollection": ".tags_collection",
    "Task": ".task",
    "TaskState": ".task_state",
    "TaskStatus": ".task_status",
    "TasksCollection": ".tasks_collection",
    "Tenant": ".tenant",
    "TowingTask": ".towing_task",
    "Uuid": ".uuid_",
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
    "CheckAvailabilityTask",
    "CollectionLinks",
    "CollectionMetadata",
    "ErrorNotFound",
    "ErrorNotFoundErrorsItem",
    "FullRefreshPersisterTask",
    "FullRefreshUploadTask",
    "GraphQlResponse",
    "Id",
    "IncrementalRefreshUploadTask",
    "LaunchJobTask",
    "OrderParametersServicePlan",
    "ServiceCredential",
    "ServiceCredentialType",
    "ServiceCredentialTypesCollection",
    "ServiceCredentialsCollection",
    "ServiceInstance",
    "ServiceInstanceNode",
    "ServiceInstanceNodesCollection",
    "ServiceInstancesCollection",
    "ServiceInventoriesCollection",
    "ServiceInventory",
    "ServiceOffering",
    "ServiceOfferingIcon",
    "ServiceOfferingIconsCollection",
    "ServiceOfferingNode",
    "ServiceOfferingNodesCollection",
    "ServiceOfferingsCollection",
    "ServicePlan",
    "ServicePlansCollection",
    "Source",
    "SourcesCollection",
    "Tag",
    "TagsCollection",
    "Task",
    "TaskState",
    "TaskStatus",
    "TasksCollection",
    "Tenant",
    "TowingTask",
    "Uuid",
]
