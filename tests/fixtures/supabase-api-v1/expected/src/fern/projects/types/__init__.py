



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .disk_request_body_attributes import (
        DiskRequestBodyAttributes,
        DiskRequestBodyAttributes_Gp3,
        DiskRequestBodyAttributes_Io2,
    )
    from .disk_request_body_attributes_gp3 import DiskRequestBodyAttributesGp3
    from .disk_request_body_attributes_io2 import DiskRequestBodyAttributesIo2
    from .network_restrictions_patch_request_add import NetworkRestrictionsPatchRequestAdd
    from .network_restrictions_patch_request_remove import NetworkRestrictionsPatchRequestRemove
    from .upgrade_database_body_release_channel import UpgradeDatabaseBodyReleaseChannel
    from .v1create_project_body_desired_instance_size import V1CreateProjectBodyDesiredInstanceSize
    from .v1create_project_body_plan import V1CreateProjectBodyPlan
    from .v1create_project_body_region import V1CreateProjectBodyRegion
    from .v1create_project_body_region_selection import (
        V1CreateProjectBodyRegionSelection,
        V1CreateProjectBodyRegionSelection_SmartGroup,
        V1CreateProjectBodyRegionSelection_Specific,
    )
    from .v1create_project_body_region_selection_smart_group import V1CreateProjectBodyRegionSelectionSmartGroup
    from .v1create_project_body_region_selection_smart_group_code import (
        V1CreateProjectBodyRegionSelectionSmartGroupCode,
    )
    from .v1create_project_body_region_selection_specific import V1CreateProjectBodyRegionSelectionSpecific
    from .v1create_project_body_region_selection_specific_code import V1CreateProjectBodyRegionSelectionSpecificCode
    from .v1get_all_projects_for_organization_request_sort import V1GetAllProjectsForOrganizationRequestSort
    from .v1get_available_regions_request_continent import V1GetAvailableRegionsRequestContinent
    from .v1get_available_regions_request_desired_instance_size import V1GetAvailableRegionsRequestDesiredInstanceSize
    from .v1get_services_health_request_services import V1GetServicesHealthRequestServices
    from .v1get_services_health_request_services_one_item import V1GetServicesHealthRequestServicesOneItem
_dynamic_imports: typing.Dict[str, str] = {
    "DiskRequestBodyAttributes": ".disk_request_body_attributes",
    "DiskRequestBodyAttributesGp3": ".disk_request_body_attributes_gp3",
    "DiskRequestBodyAttributesIo2": ".disk_request_body_attributes_io2",
    "DiskRequestBodyAttributes_Gp3": ".disk_request_body_attributes",
    "DiskRequestBodyAttributes_Io2": ".disk_request_body_attributes",
    "NetworkRestrictionsPatchRequestAdd": ".network_restrictions_patch_request_add",
    "NetworkRestrictionsPatchRequestRemove": ".network_restrictions_patch_request_remove",
    "UpgradeDatabaseBodyReleaseChannel": ".upgrade_database_body_release_channel",
    "V1CreateProjectBodyDesiredInstanceSize": ".v1create_project_body_desired_instance_size",
    "V1CreateProjectBodyPlan": ".v1create_project_body_plan",
    "V1CreateProjectBodyRegion": ".v1create_project_body_region",
    "V1CreateProjectBodyRegionSelection": ".v1create_project_body_region_selection",
    "V1CreateProjectBodyRegionSelectionSmartGroup": ".v1create_project_body_region_selection_smart_group",
    "V1CreateProjectBodyRegionSelectionSmartGroupCode": ".v1create_project_body_region_selection_smart_group_code",
    "V1CreateProjectBodyRegionSelectionSpecific": ".v1create_project_body_region_selection_specific",
    "V1CreateProjectBodyRegionSelectionSpecificCode": ".v1create_project_body_region_selection_specific_code",
    "V1CreateProjectBodyRegionSelection_SmartGroup": ".v1create_project_body_region_selection",
    "V1CreateProjectBodyRegionSelection_Specific": ".v1create_project_body_region_selection",
    "V1GetAllProjectsForOrganizationRequestSort": ".v1get_all_projects_for_organization_request_sort",
    "V1GetAvailableRegionsRequestContinent": ".v1get_available_regions_request_continent",
    "V1GetAvailableRegionsRequestDesiredInstanceSize": ".v1get_available_regions_request_desired_instance_size",
    "V1GetServicesHealthRequestServices": ".v1get_services_health_request_services",
    "V1GetServicesHealthRequestServicesOneItem": ".v1get_services_health_request_services_one_item",
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
    "DiskRequestBodyAttributes",
    "DiskRequestBodyAttributesGp3",
    "DiskRequestBodyAttributesIo2",
    "DiskRequestBodyAttributes_Gp3",
    "DiskRequestBodyAttributes_Io2",
    "NetworkRestrictionsPatchRequestAdd",
    "NetworkRestrictionsPatchRequestRemove",
    "UpgradeDatabaseBodyReleaseChannel",
    "V1CreateProjectBodyDesiredInstanceSize",
    "V1CreateProjectBodyPlan",
    "V1CreateProjectBodyRegion",
    "V1CreateProjectBodyRegionSelection",
    "V1CreateProjectBodyRegionSelectionSmartGroup",
    "V1CreateProjectBodyRegionSelectionSmartGroupCode",
    "V1CreateProjectBodyRegionSelectionSpecific",
    "V1CreateProjectBodyRegionSelectionSpecificCode",
    "V1CreateProjectBodyRegionSelection_SmartGroup",
    "V1CreateProjectBodyRegionSelection_Specific",
    "V1GetAllProjectsForOrganizationRequestSort",
    "V1GetAvailableRegionsRequestContinent",
    "V1GetAvailableRegionsRequestDesiredInstanceSize",
    "V1GetServicesHealthRequestServices",
    "V1GetServicesHealthRequestServicesOneItem",
]
