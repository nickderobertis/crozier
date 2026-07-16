



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CheckAvailabilityTask,
        CollectionLinks,
        CollectionMetadata,
        ErrorNotFound,
        ErrorNotFoundErrorsItem,
        FullRefreshPersisterTask,
        FullRefreshUploadTask,
        GraphQlResponse,
        Id,
        IncrementalRefreshUploadTask,
        LaunchJobTask,
        OrderParametersServicePlan,
        ServiceCredential,
        ServiceCredentialType,
        ServiceCredentialTypesCollection,
        ServiceCredentialsCollection,
        ServiceInstance,
        ServiceInstanceNode,
        ServiceInstanceNodesCollection,
        ServiceInstancesCollection,
        ServiceInventoriesCollection,
        ServiceInventory,
        ServiceOffering,
        ServiceOfferingIcon,
        ServiceOfferingIconsCollection,
        ServiceOfferingNode,
        ServiceOfferingNodesCollection,
        ServiceOfferingsCollection,
        ServicePlan,
        ServicePlansCollection,
        Source,
        SourcesCollection,
        Tag,
        TagsCollection,
        Task,
        TaskState,
        TaskStatus,
        TasksCollection,
        Tenant,
        TowingTask,
        Uuid,
    )
    from .errors import BadRequestError, NotFoundError, TooManyRequestsError
    from . import (
        service_credential,
        service_credential_type,
        service_instance,
        service_inventory,
        service_offering,
        service_offering_node,
        service_plan,
        source,
        tags,
        task,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .service_offering import OrderServiceOfferingResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "CheckAvailabilityTask": ".types",
    "CollectionLinks": ".types",
    "CollectionMetadata": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "ErrorNotFound": ".types",
    "ErrorNotFoundErrorsItem": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FullRefreshPersisterTask": ".types",
    "FullRefreshUploadTask": ".types",
    "GraphQlResponse": ".types",
    "Id": ".types",
    "IncrementalRefreshUploadTask": ".types",
    "LaunchJobTask": ".types",
    "NotFoundError": ".errors",
    "OrderParametersServicePlan": ".types",
    "OrderServiceOfferingResponse": ".service_offering",
    "ServiceCredential": ".types",
    "ServiceCredentialType": ".types",
    "ServiceCredentialTypesCollection": ".types",
    "ServiceCredentialsCollection": ".types",
    "ServiceInstance": ".types",
    "ServiceInstanceNode": ".types",
    "ServiceInstanceNodesCollection": ".types",
    "ServiceInstancesCollection": ".types",
    "ServiceInventoriesCollection": ".types",
    "ServiceInventory": ".types",
    "ServiceOffering": ".types",
    "ServiceOfferingIcon": ".types",
    "ServiceOfferingIconsCollection": ".types",
    "ServiceOfferingNode": ".types",
    "ServiceOfferingNodesCollection": ".types",
    "ServiceOfferingsCollection": ".types",
    "ServicePlan": ".types",
    "ServicePlansCollection": ".types",
    "Source": ".types",
    "SourcesCollection": ".types",
    "Tag": ".types",
    "TagsCollection": ".types",
    "Task": ".types",
    "TaskState": ".types",
    "TaskStatus": ".types",
    "TasksCollection": ".types",
    "Tenant": ".types",
    "TooManyRequestsError": ".errors",
    "TowingTask": ".types",
    "Uuid": ".types",
    "__version__": ".version",
    "service_credential": ".service_credential",
    "service_credential_type": ".service_credential_type",
    "service_instance": ".service_instance",
    "service_inventory": ".service_inventory",
    "service_offering": ".service_offering",
    "service_offering_node": ".service_offering_node",
    "service_plan": ".service_plan",
    "source": ".source",
    "tags": ".tags",
    "task": ".task",
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
    "BadRequestError",
    "CheckAvailabilityTask",
    "CollectionLinks",
    "CollectionMetadata",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "ErrorNotFound",
    "ErrorNotFoundErrorsItem",
    "FernApi",
    "FernApiEnvironment",
    "FullRefreshPersisterTask",
    "FullRefreshUploadTask",
    "GraphQlResponse",
    "Id",
    "IncrementalRefreshUploadTask",
    "LaunchJobTask",
    "NotFoundError",
    "OrderParametersServicePlan",
    "OrderServiceOfferingResponse",
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
    "TooManyRequestsError",
    "TowingTask",
    "Uuid",
    "__version__",
    "service_credential",
    "service_credential_type",
    "service_instance",
    "service_inventory",
    "service_offering",
    "service_offering_node",
    "service_plan",
    "source",
    "tags",
    "task",
]
