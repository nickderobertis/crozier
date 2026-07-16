



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .tenancy_contact_assignments_list_response import TenancyContactAssignmentsListResponse
    from .tenancy_contact_groups_list_response import TenancyContactGroupsListResponse
    from .tenancy_contact_roles_list_response import TenancyContactRolesListResponse
    from .tenancy_contacts_list_response import TenancyContactsListResponse
    from .tenancy_tenant_groups_list_response import TenancyTenantGroupsListResponse
    from .tenancy_tenants_list_response import TenancyTenantsListResponse
_dynamic_imports: typing.Dict[str, str] = {
    "TenancyContactAssignmentsListResponse": ".tenancy_contact_assignments_list_response",
    "TenancyContactGroupsListResponse": ".tenancy_contact_groups_list_response",
    "TenancyContactRolesListResponse": ".tenancy_contact_roles_list_response",
    "TenancyContactsListResponse": ".tenancy_contacts_list_response",
    "TenancyTenantGroupsListResponse": ".tenancy_tenant_groups_list_response",
    "TenancyTenantsListResponse": ".tenancy_tenants_list_response",
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
    "TenancyContactAssignmentsListResponse",
    "TenancyContactGroupsListResponse",
    "TenancyContactRolesListResponse",
    "TenancyContactsListResponse",
    "TenancyTenantGroupsListResponse",
    "TenancyTenantsListResponse",
]
