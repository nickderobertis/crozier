



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get11account_id_clients_request_show import Get11AccountIdClientsRequestShow
    from .v1companies_create_client import V1CompaniesCreateClient
    from .v1companies_create_client_external_references_item import V1CompaniesCreateClientExternalReferencesItem
    from .v1companies_update_client import V1CompaniesUpdateClient
    from .v1companies_update_client_external_references_item import V1CompaniesUpdateClientExternalReferencesItem
_dynamic_imports: typing.Dict[str, str] = {
    "Get11AccountIdClientsRequestShow": ".get11account_id_clients_request_show",
    "V1CompaniesCreateClient": ".v1companies_create_client",
    "V1CompaniesCreateClientExternalReferencesItem": ".v1companies_create_client_external_references_item",
    "V1CompaniesUpdateClient": ".v1companies_update_client",
    "V1CompaniesUpdateClientExternalReferencesItem": ".v1companies_update_client_external_references_item",
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
    "Get11AccountIdClientsRequestShow",
    "V1CompaniesCreateClient",
    "V1CompaniesCreateClientExternalReferencesItem",
    "V1CompaniesUpdateClient",
    "V1CompaniesUpdateClientExternalReferencesItem",
]
