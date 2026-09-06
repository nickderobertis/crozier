



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .servicebroker_projects_brokers_instances_service_bindings_list_request_alt import (
        ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt,
    )
    from .servicebroker_projects_brokers_instances_service_bindings_list_request_xgafv import (
        ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv,
    )
    from .servicebroker_projects_brokers_service_instances_list_request_alt import (
        ServicebrokerProjectsBrokersServiceInstancesListRequestAlt,
    )
    from .servicebroker_projects_brokers_service_instances_list_request_xgafv import (
        ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2catalog_list_request_alt import (
        ServicebrokerProjectsBrokersV2CatalogListRequestAlt,
    )
    from .servicebroker_projects_brokers_v2catalog_list_request_xgafv import (
        ServicebrokerProjectsBrokersV2CatalogListRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2service_instances_create_request_alt import (
        ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt,
    )
    from .servicebroker_projects_brokers_v2service_instances_create_request_xgafv import (
        ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2service_instances_delete_request_alt import (
        ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt,
    )
    from .servicebroker_projects_brokers_v2service_instances_delete_request_xgafv import (
        ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2service_instances_get_last_operation_request_alt import (
        ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt,
    )
    from .servicebroker_projects_brokers_v2service_instances_get_last_operation_request_xgafv import (
        ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2service_instances_get_request_alt import (
        ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt,
    )
    from .servicebroker_projects_brokers_v2service_instances_get_request_xgafv import (
        ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2service_instances_patch_request_alt import (
        ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt,
    )
    from .servicebroker_projects_brokers_v2service_instances_patch_request_xgafv import (
        ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2service_instances_service_bindings_create_request_alt import (
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt,
    )
    from .servicebroker_projects_brokers_v2service_instances_service_bindings_create_request_xgafv import (
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation_request_alt import (
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt,
    )
    from .servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation_request_xgafv import (
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv,
    )
    from .servicebroker_projects_brokers_v2service_instances_service_bindings_get_request_alt import (
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt,
    )
    from .servicebroker_projects_brokers_v2service_instances_service_bindings_get_request_xgafv import (
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt": ".servicebroker_projects_brokers_instances_service_bindings_list_request_alt",
    "ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv": ".servicebroker_projects_brokers_instances_service_bindings_list_request_xgafv",
    "ServicebrokerProjectsBrokersServiceInstancesListRequestAlt": ".servicebroker_projects_brokers_service_instances_list_request_alt",
    "ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv": ".servicebroker_projects_brokers_service_instances_list_request_xgafv",
    "ServicebrokerProjectsBrokersV2CatalogListRequestAlt": ".servicebroker_projects_brokers_v2catalog_list_request_alt",
    "ServicebrokerProjectsBrokersV2CatalogListRequestXgafv": ".servicebroker_projects_brokers_v2catalog_list_request_xgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt": ".servicebroker_projects_brokers_v2service_instances_create_request_alt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv": ".servicebroker_projects_brokers_v2service_instances_create_request_xgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt": ".servicebroker_projects_brokers_v2service_instances_delete_request_alt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv": ".servicebroker_projects_brokers_v2service_instances_delete_request_xgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt": ".servicebroker_projects_brokers_v2service_instances_get_last_operation_request_alt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv": ".servicebroker_projects_brokers_v2service_instances_get_last_operation_request_xgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt": ".servicebroker_projects_brokers_v2service_instances_get_request_alt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv": ".servicebroker_projects_brokers_v2service_instances_get_request_xgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt": ".servicebroker_projects_brokers_v2service_instances_patch_request_alt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv": ".servicebroker_projects_brokers_v2service_instances_patch_request_xgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt": ".servicebroker_projects_brokers_v2service_instances_service_bindings_create_request_alt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv": ".servicebroker_projects_brokers_v2service_instances_service_bindings_create_request_xgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt": ".servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation_request_alt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv": ".servicebroker_projects_brokers_v2service_instances_service_bindings_get_last_operation_request_xgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt": ".servicebroker_projects_brokers_v2service_instances_service_bindings_get_request_alt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv": ".servicebroker_projects_brokers_v2service_instances_service_bindings_get_request_xgafv",
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
    "ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt",
    "ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv",
    "ServicebrokerProjectsBrokersServiceInstancesListRequestAlt",
    "ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv",
    "ServicebrokerProjectsBrokersV2CatalogListRequestAlt",
    "ServicebrokerProjectsBrokersV2CatalogListRequestXgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv",
]
