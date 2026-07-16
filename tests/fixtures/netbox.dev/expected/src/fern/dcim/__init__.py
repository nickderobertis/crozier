



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DcimCableTerminationsListResponse,
        DcimCablesListResponse,
        DcimConsolePortTemplatesListResponse,
        DcimConsolePortsListResponse,
        DcimConsoleServerPortTemplatesListResponse,
        DcimConsoleServerPortsListResponse,
        DcimDeviceBayTemplatesListResponse,
        DcimDeviceBaysListResponse,
        DcimDeviceRolesListResponse,
        DcimDeviceTypesListResponse,
        DcimDevicesListResponse,
        DcimFrontPortTemplatesListResponse,
        DcimFrontPortsListResponse,
        DcimInterfaceTemplatesListResponse,
        DcimInterfacesListResponse,
        DcimInventoryItemRolesListResponse,
        DcimInventoryItemTemplatesListResponse,
        DcimInventoryItemsListResponse,
        DcimLocationsListResponse,
        DcimManufacturersListResponse,
        DcimModuleBayTemplatesListResponse,
        DcimModuleBaysListResponse,
        DcimModuleTypesListResponse,
        DcimModulesListResponse,
        DcimPlatformsListResponse,
        DcimPowerFeedsListResponse,
        DcimPowerOutletTemplatesListResponse,
        DcimPowerOutletsListResponse,
        DcimPowerPanelsListResponse,
        DcimPowerPortTemplatesListResponse,
        DcimPowerPortsListResponse,
        DcimRackReservationsListResponse,
        DcimRackRolesListResponse,
        DcimRacksElevationRequestFace,
        DcimRacksElevationRequestRender,
        DcimRacksListResponse,
        DcimRearPortTemplatesListResponse,
        DcimRearPortsListResponse,
        DcimRegionsListResponse,
        DcimSiteGroupsListResponse,
        DcimSitesListResponse,
        DcimVirtualChassisListResponse,
        DcimVirtualDeviceContextsListResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DcimCableTerminationsListResponse": ".types",
    "DcimCablesListResponse": ".types",
    "DcimConsolePortTemplatesListResponse": ".types",
    "DcimConsolePortsListResponse": ".types",
    "DcimConsoleServerPortTemplatesListResponse": ".types",
    "DcimConsoleServerPortsListResponse": ".types",
    "DcimDeviceBayTemplatesListResponse": ".types",
    "DcimDeviceBaysListResponse": ".types",
    "DcimDeviceRolesListResponse": ".types",
    "DcimDeviceTypesListResponse": ".types",
    "DcimDevicesListResponse": ".types",
    "DcimFrontPortTemplatesListResponse": ".types",
    "DcimFrontPortsListResponse": ".types",
    "DcimInterfaceTemplatesListResponse": ".types",
    "DcimInterfacesListResponse": ".types",
    "DcimInventoryItemRolesListResponse": ".types",
    "DcimInventoryItemTemplatesListResponse": ".types",
    "DcimInventoryItemsListResponse": ".types",
    "DcimLocationsListResponse": ".types",
    "DcimManufacturersListResponse": ".types",
    "DcimModuleBayTemplatesListResponse": ".types",
    "DcimModuleBaysListResponse": ".types",
    "DcimModuleTypesListResponse": ".types",
    "DcimModulesListResponse": ".types",
    "DcimPlatformsListResponse": ".types",
    "DcimPowerFeedsListResponse": ".types",
    "DcimPowerOutletTemplatesListResponse": ".types",
    "DcimPowerOutletsListResponse": ".types",
    "DcimPowerPanelsListResponse": ".types",
    "DcimPowerPortTemplatesListResponse": ".types",
    "DcimPowerPortsListResponse": ".types",
    "DcimRackReservationsListResponse": ".types",
    "DcimRackRolesListResponse": ".types",
    "DcimRacksElevationRequestFace": ".types",
    "DcimRacksElevationRequestRender": ".types",
    "DcimRacksListResponse": ".types",
    "DcimRearPortTemplatesListResponse": ".types",
    "DcimRearPortsListResponse": ".types",
    "DcimRegionsListResponse": ".types",
    "DcimSiteGroupsListResponse": ".types",
    "DcimSitesListResponse": ".types",
    "DcimVirtualChassisListResponse": ".types",
    "DcimVirtualDeviceContextsListResponse": ".types",
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
