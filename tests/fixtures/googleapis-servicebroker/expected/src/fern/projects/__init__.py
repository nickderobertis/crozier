



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
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
_dynamic_imports: typing.Dict[str, str] = {
    "ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestAlt": ".types",
    "ServicebrokerProjectsBrokersInstancesServiceBindingsListRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersServiceInstancesListRequestAlt": ".types",
    "ServicebrokerProjectsBrokersServiceInstancesListRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2CatalogListRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2CatalogListRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesCreateRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesDeleteRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetLastOperationRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesGetRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesPatchRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsCreateRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetLastOperationRequestXgafv": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestAlt": ".types",
    "ServicebrokerProjectsBrokersV2ServiceInstancesServiceBindingsGetRequestXgafv": ".types",
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
