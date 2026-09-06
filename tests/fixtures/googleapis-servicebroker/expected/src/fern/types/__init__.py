



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .google_cloud_servicebroker_v1alpha1binding import GoogleCloudServicebrokerV1Alpha1Binding
    from .google_cloud_servicebroker_v1alpha1create_binding_response import (
        GoogleCloudServicebrokerV1Alpha1CreateBindingResponse,
    )
    from .google_cloud_servicebroker_v1alpha1create_service_instance_response import (
        GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse,
    )
    from .google_cloud_servicebroker_v1alpha1dashboard_client import GoogleCloudServicebrokerV1Alpha1DashboardClient
    from .google_cloud_servicebroker_v1alpha1delete_binding_response import (
        GoogleCloudServicebrokerV1Alpha1DeleteBindingResponse,
    )
    from .google_cloud_servicebroker_v1alpha1delete_service_instance_response import (
        GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse,
    )
    from .google_cloud_servicebroker_v1alpha1get_binding_response import (
        GoogleCloudServicebrokerV1Alpha1GetBindingResponse,
    )
    from .google_cloud_servicebroker_v1alpha1list_bindings_response import (
        GoogleCloudServicebrokerV1Alpha1ListBindingsResponse,
    )
    from .google_cloud_servicebroker_v1alpha1list_catalog_response import (
        GoogleCloudServicebrokerV1Alpha1ListCatalogResponse,
    )
    from .google_cloud_servicebroker_v1alpha1list_service_instances_response import (
        GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse,
    )
    from .google_cloud_servicebroker_v1alpha1operation import GoogleCloudServicebrokerV1Alpha1Operation
    from .google_cloud_servicebroker_v1alpha1plan import GoogleCloudServicebrokerV1Alpha1Plan
    from .google_cloud_servicebroker_v1alpha1service import GoogleCloudServicebrokerV1Alpha1Service
    from .google_cloud_servicebroker_v1alpha1service_instance import GoogleCloudServicebrokerV1Alpha1ServiceInstance
    from .google_cloud_servicebroker_v1alpha1update_service_instance_response import (
        GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse,
    )
    from .google_iam_v1binding import GoogleIamV1Binding
    from .google_iam_v1policy import GoogleIamV1Policy
    from .google_iam_v1test_iam_permissions_response import GoogleIamV1TestIamPermissionsResponse
    from .google_type_expr import GoogleTypeExpr
    from .oauth_scope import OauthScope
_dynamic_imports: typing.Dict[str, str] = {
    "GoogleCloudServicebrokerV1Alpha1Binding": ".google_cloud_servicebroker_v1alpha1binding",
    "GoogleCloudServicebrokerV1Alpha1CreateBindingResponse": ".google_cloud_servicebroker_v1alpha1create_binding_response",
    "GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse": ".google_cloud_servicebroker_v1alpha1create_service_instance_response",
    "GoogleCloudServicebrokerV1Alpha1DashboardClient": ".google_cloud_servicebroker_v1alpha1dashboard_client",
    "GoogleCloudServicebrokerV1Alpha1DeleteBindingResponse": ".google_cloud_servicebroker_v1alpha1delete_binding_response",
    "GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse": ".google_cloud_servicebroker_v1alpha1delete_service_instance_response",
    "GoogleCloudServicebrokerV1Alpha1GetBindingResponse": ".google_cloud_servicebroker_v1alpha1get_binding_response",
    "GoogleCloudServicebrokerV1Alpha1ListBindingsResponse": ".google_cloud_servicebroker_v1alpha1list_bindings_response",
    "GoogleCloudServicebrokerV1Alpha1ListCatalogResponse": ".google_cloud_servicebroker_v1alpha1list_catalog_response",
    "GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse": ".google_cloud_servicebroker_v1alpha1list_service_instances_response",
    "GoogleCloudServicebrokerV1Alpha1Operation": ".google_cloud_servicebroker_v1alpha1operation",
    "GoogleCloudServicebrokerV1Alpha1Plan": ".google_cloud_servicebroker_v1alpha1plan",
    "GoogleCloudServicebrokerV1Alpha1Service": ".google_cloud_servicebroker_v1alpha1service",
    "GoogleCloudServicebrokerV1Alpha1ServiceInstance": ".google_cloud_servicebroker_v1alpha1service_instance",
    "GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse": ".google_cloud_servicebroker_v1alpha1update_service_instance_response",
    "GoogleIamV1Binding": ".google_iam_v1binding",
    "GoogleIamV1Policy": ".google_iam_v1policy",
    "GoogleIamV1TestIamPermissionsResponse": ".google_iam_v1test_iam_permissions_response",
    "GoogleTypeExpr": ".google_type_expr",
    "OauthScope": ".oauth_scope",
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
    "GoogleCloudServicebrokerV1Alpha1Binding",
    "GoogleCloudServicebrokerV1Alpha1CreateBindingResponse",
    "GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse",
    "GoogleCloudServicebrokerV1Alpha1DashboardClient",
    "GoogleCloudServicebrokerV1Alpha1DeleteBindingResponse",
    "GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse",
    "GoogleCloudServicebrokerV1Alpha1GetBindingResponse",
    "GoogleCloudServicebrokerV1Alpha1ListBindingsResponse",
    "GoogleCloudServicebrokerV1Alpha1ListCatalogResponse",
    "GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse",
    "GoogleCloudServicebrokerV1Alpha1Operation",
    "GoogleCloudServicebrokerV1Alpha1Plan",
    "GoogleCloudServicebrokerV1Alpha1Service",
    "GoogleCloudServicebrokerV1Alpha1ServiceInstance",
    "GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse",
    "GoogleIamV1Binding",
    "GoogleIamV1Policy",
    "GoogleIamV1TestIamPermissionsResponse",
    "GoogleTypeExpr",
    "OauthScope",
]
