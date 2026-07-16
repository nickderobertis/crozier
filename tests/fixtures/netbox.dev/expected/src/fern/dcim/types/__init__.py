



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .dcim_cable_terminations_list_response import DcimCableTerminationsListResponse
    from .dcim_cables_list_response import DcimCablesListResponse
    from .dcim_console_port_templates_list_response import DcimConsolePortTemplatesListResponse
    from .dcim_console_ports_list_response import DcimConsolePortsListResponse
    from .dcim_console_server_port_templates_list_response import DcimConsoleServerPortTemplatesListResponse
    from .dcim_console_server_ports_list_response import DcimConsoleServerPortsListResponse
    from .dcim_device_bay_templates_list_response import DcimDeviceBayTemplatesListResponse
    from .dcim_device_bays_list_response import DcimDeviceBaysListResponse
    from .dcim_device_roles_list_response import DcimDeviceRolesListResponse
    from .dcim_device_types_list_response import DcimDeviceTypesListResponse
    from .dcim_devices_list_response import DcimDevicesListResponse
    from .dcim_front_port_templates_list_response import DcimFrontPortTemplatesListResponse
    from .dcim_front_ports_list_response import DcimFrontPortsListResponse
    from .dcim_interface_templates_list_response import DcimInterfaceTemplatesListResponse
    from .dcim_interfaces_list_response import DcimInterfacesListResponse
    from .dcim_inventory_item_roles_list_response import DcimInventoryItemRolesListResponse
    from .dcim_inventory_item_templates_list_response import DcimInventoryItemTemplatesListResponse
    from .dcim_inventory_items_list_response import DcimInventoryItemsListResponse
    from .dcim_locations_list_response import DcimLocationsListResponse
    from .dcim_manufacturers_list_response import DcimManufacturersListResponse
    from .dcim_module_bay_templates_list_response import DcimModuleBayTemplatesListResponse
    from .dcim_module_bays_list_response import DcimModuleBaysListResponse
    from .dcim_module_types_list_response import DcimModuleTypesListResponse
    from .dcim_modules_list_response import DcimModulesListResponse
    from .dcim_platforms_list_response import DcimPlatformsListResponse
    from .dcim_power_feeds_list_response import DcimPowerFeedsListResponse
    from .dcim_power_outlet_templates_list_response import DcimPowerOutletTemplatesListResponse
    from .dcim_power_outlets_list_response import DcimPowerOutletsListResponse
    from .dcim_power_panels_list_response import DcimPowerPanelsListResponse
    from .dcim_power_port_templates_list_response import DcimPowerPortTemplatesListResponse
    from .dcim_power_ports_list_response import DcimPowerPortsListResponse
    from .dcim_rack_reservations_list_response import DcimRackReservationsListResponse
    from .dcim_rack_roles_list_response import DcimRackRolesListResponse
    from .dcim_racks_elevation_request_face import DcimRacksElevationRequestFace
    from .dcim_racks_elevation_request_render import DcimRacksElevationRequestRender
    from .dcim_racks_list_response import DcimRacksListResponse
    from .dcim_rear_port_templates_list_response import DcimRearPortTemplatesListResponse
    from .dcim_rear_ports_list_response import DcimRearPortsListResponse
    from .dcim_regions_list_response import DcimRegionsListResponse
    from .dcim_site_groups_list_response import DcimSiteGroupsListResponse
    from .dcim_sites_list_response import DcimSitesListResponse
    from .dcim_virtual_chassis_list_response import DcimVirtualChassisListResponse
    from .dcim_virtual_device_contexts_list_response import DcimVirtualDeviceContextsListResponse
_dynamic_imports: typing.Dict[str, str] = {
    "DcimCableTerminationsListResponse": ".dcim_cable_terminations_list_response",
    "DcimCablesListResponse": ".dcim_cables_list_response",
    "DcimConsolePortTemplatesListResponse": ".dcim_console_port_templates_list_response",
    "DcimConsolePortsListResponse": ".dcim_console_ports_list_response",
    "DcimConsoleServerPortTemplatesListResponse": ".dcim_console_server_port_templates_list_response",
    "DcimConsoleServerPortsListResponse": ".dcim_console_server_ports_list_response",
    "DcimDeviceBayTemplatesListResponse": ".dcim_device_bay_templates_list_response",
    "DcimDeviceBaysListResponse": ".dcim_device_bays_list_response",
    "DcimDeviceRolesListResponse": ".dcim_device_roles_list_response",
    "DcimDeviceTypesListResponse": ".dcim_device_types_list_response",
    "DcimDevicesListResponse": ".dcim_devices_list_response",
    "DcimFrontPortTemplatesListResponse": ".dcim_front_port_templates_list_response",
    "DcimFrontPortsListResponse": ".dcim_front_ports_list_response",
    "DcimInterfaceTemplatesListResponse": ".dcim_interface_templates_list_response",
    "DcimInterfacesListResponse": ".dcim_interfaces_list_response",
    "DcimInventoryItemRolesListResponse": ".dcim_inventory_item_roles_list_response",
    "DcimInventoryItemTemplatesListResponse": ".dcim_inventory_item_templates_list_response",
    "DcimInventoryItemsListResponse": ".dcim_inventory_items_list_response",
    "DcimLocationsListResponse": ".dcim_locations_list_response",
    "DcimManufacturersListResponse": ".dcim_manufacturers_list_response",
    "DcimModuleBayTemplatesListResponse": ".dcim_module_bay_templates_list_response",
    "DcimModuleBaysListResponse": ".dcim_module_bays_list_response",
    "DcimModuleTypesListResponse": ".dcim_module_types_list_response",
    "DcimModulesListResponse": ".dcim_modules_list_response",
    "DcimPlatformsListResponse": ".dcim_platforms_list_response",
    "DcimPowerFeedsListResponse": ".dcim_power_feeds_list_response",
    "DcimPowerOutletTemplatesListResponse": ".dcim_power_outlet_templates_list_response",
    "DcimPowerOutletsListResponse": ".dcim_power_outlets_list_response",
    "DcimPowerPanelsListResponse": ".dcim_power_panels_list_response",
    "DcimPowerPortTemplatesListResponse": ".dcim_power_port_templates_list_response",
    "DcimPowerPortsListResponse": ".dcim_power_ports_list_response",
    "DcimRackReservationsListResponse": ".dcim_rack_reservations_list_response",
    "DcimRackRolesListResponse": ".dcim_rack_roles_list_response",
    "DcimRacksElevationRequestFace": ".dcim_racks_elevation_request_face",
    "DcimRacksElevationRequestRender": ".dcim_racks_elevation_request_render",
    "DcimRacksListResponse": ".dcim_racks_list_response",
    "DcimRearPortTemplatesListResponse": ".dcim_rear_port_templates_list_response",
    "DcimRearPortsListResponse": ".dcim_rear_ports_list_response",
    "DcimRegionsListResponse": ".dcim_regions_list_response",
    "DcimSiteGroupsListResponse": ".dcim_site_groups_list_response",
    "DcimSitesListResponse": ".dcim_sites_list_response",
    "DcimVirtualChassisListResponse": ".dcim_virtual_chassis_list_response",
    "DcimVirtualDeviceContextsListResponse": ".dcim_virtual_device_contexts_list_response",
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
    "DcimCableTerminationsListResponse",
    "DcimCablesListResponse",
    "DcimConsolePortTemplatesListResponse",
    "DcimConsolePortsListResponse",
    "DcimConsoleServerPortTemplatesListResponse",
    "DcimConsoleServerPortsListResponse",
    "DcimDeviceBayTemplatesListResponse",
    "DcimDeviceBaysListResponse",
    "DcimDeviceRolesListResponse",
    "DcimDeviceTypesListResponse",
    "DcimDevicesListResponse",
    "DcimFrontPortTemplatesListResponse",
    "DcimFrontPortsListResponse",
    "DcimInterfaceTemplatesListResponse",
    "DcimInterfacesListResponse",
    "DcimInventoryItemRolesListResponse",
    "DcimInventoryItemTemplatesListResponse",
    "DcimInventoryItemsListResponse",
    "DcimLocationsListResponse",
    "DcimManufacturersListResponse",
    "DcimModuleBayTemplatesListResponse",
    "DcimModuleBaysListResponse",
    "DcimModuleTypesListResponse",
    "DcimModulesListResponse",
    "DcimPlatformsListResponse",
    "DcimPowerFeedsListResponse",
    "DcimPowerOutletTemplatesListResponse",
    "DcimPowerOutletsListResponse",
    "DcimPowerPanelsListResponse",
    "DcimPowerPortTemplatesListResponse",
    "DcimPowerPortsListResponse",
    "DcimRackReservationsListResponse",
    "DcimRackRolesListResponse",
    "DcimRacksElevationRequestFace",
    "DcimRacksElevationRequestRender",
    "DcimRacksListResponse",
    "DcimRearPortTemplatesListResponse",
    "DcimRearPortsListResponse",
    "DcimRegionsListResponse",
    "DcimSiteGroupsListResponse",
    "DcimSitesListResponse",
    "DcimVirtualChassisListResponse",
    "DcimVirtualDeviceContextsListResponse",
]
