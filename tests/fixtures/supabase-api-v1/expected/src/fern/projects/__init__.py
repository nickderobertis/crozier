



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        DiskRequestBodyAttributes,
        DiskRequestBodyAttributesGp3,
        DiskRequestBodyAttributesIo2,
        DiskRequestBodyAttributes_Gp3,
        DiskRequestBodyAttributes_Io2,
        NetworkRestrictionsPatchRequestAdd,
        NetworkRestrictionsPatchRequestRemove,
        UpgradeDatabaseBodyReleaseChannel,
        V1CreateProjectBodyDesiredInstanceSize,
        V1CreateProjectBodyPlan,
        V1CreateProjectBodyRegion,
        V1CreateProjectBodyRegionSelection,
        V1CreateProjectBodyRegionSelectionSmartGroup,
        V1CreateProjectBodyRegionSelectionSmartGroupCode,
        V1CreateProjectBodyRegionSelectionSpecific,
        V1CreateProjectBodyRegionSelectionSpecificCode,
        V1CreateProjectBodyRegionSelection_SmartGroup,
        V1CreateProjectBodyRegionSelection_Specific,
        V1GetAllProjectsForOrganizationRequestSort,
        V1GetAvailableRegionsRequestContinent,
        V1GetAvailableRegionsRequestDesiredInstanceSize,
        V1GetServicesHealthRequestServices,
        V1GetServicesHealthRequestServicesOneItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "DiskRequestBodyAttributes": ".types",
    "DiskRequestBodyAttributesGp3": ".types",
    "DiskRequestBodyAttributesIo2": ".types",
    "DiskRequestBodyAttributes_Gp3": ".types",
    "DiskRequestBodyAttributes_Io2": ".types",
    "NetworkRestrictionsPatchRequestAdd": ".types",
    "NetworkRestrictionsPatchRequestRemove": ".types",
    "UpgradeDatabaseBodyReleaseChannel": ".types",
    "V1CreateProjectBodyDesiredInstanceSize": ".types",
    "V1CreateProjectBodyPlan": ".types",
    "V1CreateProjectBodyRegion": ".types",
    "V1CreateProjectBodyRegionSelection": ".types",
    "V1CreateProjectBodyRegionSelectionSmartGroup": ".types",
    "V1CreateProjectBodyRegionSelectionSmartGroupCode": ".types",
    "V1CreateProjectBodyRegionSelectionSpecific": ".types",
    "V1CreateProjectBodyRegionSelectionSpecificCode": ".types",
    "V1CreateProjectBodyRegionSelection_SmartGroup": ".types",
    "V1CreateProjectBodyRegionSelection_Specific": ".types",
    "V1GetAllProjectsForOrganizationRequestSort": ".types",
    "V1GetAvailableRegionsRequestContinent": ".types",
    "V1GetAvailableRegionsRequestDesiredInstanceSize": ".types",
    "V1GetServicesHealthRequestServices": ".types",
    "V1GetServicesHealthRequestServicesOneItem": ".types",
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
