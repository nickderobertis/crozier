



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GoogleCloudServicebrokerV1Alpha1Binding,
        GoogleCloudServicebrokerV1Alpha1CreateBindingResponse,
        GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse,
        GoogleCloudServicebrokerV1Alpha1DashboardClient,
        GoogleCloudServicebrokerV1Alpha1DeleteBindingResponse,
        GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse,
        GoogleCloudServicebrokerV1Alpha1GetBindingResponse,
        GoogleCloudServicebrokerV1Alpha1ListBindingsResponse,
        GoogleCloudServicebrokerV1Alpha1ListCatalogResponse,
        GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse,
        GoogleCloudServicebrokerV1Alpha1Operation,
        GoogleCloudServicebrokerV1Alpha1Plan,
        GoogleCloudServicebrokerV1Alpha1Service,
        GoogleCloudServicebrokerV1Alpha1ServiceInstance,
        GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse,
        GoogleIamV1Binding,
        GoogleIamV1Policy,
        GoogleIamV1TestIamPermissionsResponse,
        GoogleTypeExpr,
        OauthScope,
    )
    from . import projects, v1alpha1
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .projects import (
        ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt,
        ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv,
        ServicebrokerProjectsBrokersServiceInstancesListRequestAlt,
        ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv,
        ServicebrokerProjectsBrokersV2CatalogListRequestAlt,
        ServicebrokerProjectsBrokersV2CatalogListRequestXgafv,
        ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt,
        ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv,
        ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt,
        ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv,
        ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt,
        ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv,
        ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt,
        ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv,
        ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt,
        ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv,
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt,
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv,
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt,
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv,
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt,
        ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv,
    )
    from .v1alpha1 import (
        ServicebrokerGetIamPolicyRequestAlt,
        ServicebrokerGetIamPolicyRequestXgafv,
        ServicebrokerSetIamPolicyRequestAlt,
        ServicebrokerSetIamPolicyRequestXgafv,
        ServicebrokerTestIamPermissionsRequestAlt,
        ServicebrokerTestIamPermissionsRequestXgafv,
    )
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GoogleCloudServicebrokerV1Alpha1Binding": ".types",
    "GoogleCloudServicebrokerV1Alpha1CreateBindingResponse": ".types",
    "GoogleCloudServicebrokerV1Alpha1CreateServiceInstanceResponse": ".types",
    "GoogleCloudServicebrokerV1Alpha1DashboardClient": ".types",
    "GoogleCloudServicebrokerV1Alpha1DeleteBindingResponse": ".types",
    "GoogleCloudServicebrokerV1Alpha1DeleteServiceInstanceResponse": ".types",
    "GoogleCloudServicebrokerV1Alpha1GetBindingResponse": ".types",
    "GoogleCloudServicebrokerV1Alpha1ListBindingsResponse": ".types",
    "GoogleCloudServicebrokerV1Alpha1ListCatalogResponse": ".types",
    "GoogleCloudServicebrokerV1Alpha1ListServiceInstancesResponse": ".types",
    "GoogleCloudServicebrokerV1Alpha1Operation": ".types",
    "GoogleCloudServicebrokerV1Alpha1Plan": ".types",
    "GoogleCloudServicebrokerV1Alpha1Service": ".types",
    "GoogleCloudServicebrokerV1Alpha1ServiceInstance": ".types",
    "GoogleCloudServicebrokerV1Alpha1UpdateServiceInstanceResponse": ".types",
    "GoogleIamV1Binding": ".types",
    "GoogleIamV1Policy": ".types",
    "GoogleIamV1TestIamPermissionsResponse": ".types",
    "GoogleTypeExpr": ".types",
    "OauthScope": ".types",
    "ServicebrokerGetIamPolicyRequestAlt": ".v1alpha1",
    "ServicebrokerGetIamPolicyRequestXgafv": ".v1alpha1",
    "ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersServiceInstancesListRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2CatalogListRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2CatalogListRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt": ".projects",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv": ".projects",
    "ServicebrokerSetIamPolicyRequestAlt": ".v1alpha1",
    "ServicebrokerSetIamPolicyRequestXgafv": ".v1alpha1",
    "ServicebrokerTestIamPermissionsRequestAlt": ".v1alpha1",
    "ServicebrokerTestIamPermissionsRequestXgafv": ".v1alpha1",
    "__version__": ".version",
    "projects": ".projects",
    "v1alpha1": ".v1alpha1",
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
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
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
    "ServicebrokerGetIamPolicyRequestAlt",
    "ServicebrokerGetIamPolicyRequestXgafv",
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
    "ServicebrokerSetIamPolicyRequestAlt",
    "ServicebrokerSetIamPolicyRequestXgafv",
    "ServicebrokerTestIamPermissionsRequestAlt",
    "ServicebrokerTestIamPermissionsRequestXgafv",
    "__version__",
    "projects",
    "v1alpha1",
]
