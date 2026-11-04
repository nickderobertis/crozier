



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .action_status import ActionStatus
    from .actions_definition import ActionsDefinition
    from .actions_definition_actions_item import ActionsDefinitionActionsItem
    from .actions_definition_actions_item_requests_item import ActionsDefinitionActionsItemRequestsItem
    from .actions_definition_actions_item_requests_item_http import ActionsDefinitionActionsItemRequestsItemHttp
    from .actions_definition_actions_item_requests_item_http_method import (
        ActionsDefinitionActionsItemRequestsItemHttpMethod,
    )
    from .actions_definition_actions_item_requests_item_modbus import ActionsDefinitionActionsItemRequestsItemModbus
    from .actions_definition_actions_item_requests_item_modbus_type import (
        ActionsDefinitionActionsItemRequestsItemModbusType,
    )
    from .actions_definition_const_value import ActionsDefinitionConstValue
    from .bad_request_error_body import BadRequestErrorBody
    from .conflict_error_body import ConflictErrorBody
    from .content_too_large_error_body import ContentTooLargeErrorBody
    from .directory_entry import DirectoryEntry
    from .directory_entry_type import DirectoryEntryType
    from .directory_listing import DirectoryListing
    from .directory_listing_files_item import DirectoryListingFilesItem
    from .directory_listing_files_item_type import DirectoryListingFilesItemType
    from .error import Error
    from .ethernet_settings import EthernetSettings
    from .internal_server_error_body import InternalServerErrorBody
    from .not_found_error_body import NotFoundErrorBody
    from .report_envelope import ReportEnvelope
    from .report_envelope_meter import ReportEnvelopeMeter
    from .report_envelope_report import ReportEnvelopeReport
    from .report_envelope_report_volume_item import ReportEnvelopeReportVolumeItem
    from .report_envelope_system import ReportEnvelopeSystem
    from .service_unavailable_error_body import ServiceUnavailableErrorBody
    from .settings import Settings
    from .settings_services import SettingsServices
    from .settings_services_berry import SettingsServicesBerry
    from .settings_services_cloud import SettingsServicesCloud
    from .settings_services_local import SettingsServicesLocal
    from .settings_services_modbus import SettingsServicesModbus
    from .settings_services_sd import SettingsServicesSd
    from .settings_system import SettingsSystem
    from .system_info import SystemInfo
    from .system_info_device import SystemInfoDevice
    from .system_info_meter import SystemInfoMeter
    from .system_info_wifi import SystemInfoWifi
    from .too_many_requests_error_body import TooManyRequestsErrorBody
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .unsupported_media_type_error_body import UnsupportedMediaTypeErrorBody
    from .wi_fi_network import WiFiNetwork
    from .wi_fi_sta_settings import WiFiStaSettings
_dynamic_imports: typing.Dict[str, str] = {
    "ActionStatus": ".action_status",
    "ActionsDefinition": ".actions_definition",
    "ActionsDefinitionActionsItem": ".actions_definition_actions_item",
    "ActionsDefinitionActionsItemRequestsItem": ".actions_definition_actions_item_requests_item",
    "ActionsDefinitionActionsItemRequestsItemHttp": ".actions_definition_actions_item_requests_item_http",
    "ActionsDefinitionActionsItemRequestsItemHttpMethod": ".actions_definition_actions_item_requests_item_http_method",
    "ActionsDefinitionActionsItemRequestsItemModbus": ".actions_definition_actions_item_requests_item_modbus",
    "ActionsDefinitionActionsItemRequestsItemModbusType": ".actions_definition_actions_item_requests_item_modbus_type",
    "ActionsDefinitionConstValue": ".actions_definition_const_value",
    "BadRequestErrorBody": ".bad_request_error_body",
    "ConflictErrorBody": ".conflict_error_body",
    "ContentTooLargeErrorBody": ".content_too_large_error_body",
    "DirectoryEntry": ".directory_entry",
    "DirectoryEntryType": ".directory_entry_type",
    "DirectoryListing": ".directory_listing",
    "DirectoryListingFilesItem": ".directory_listing_files_item",
    "DirectoryListingFilesItemType": ".directory_listing_files_item_type",
    "Error": ".error",
    "EthernetSettings": ".ethernet_settings",
    "InternalServerErrorBody": ".internal_server_error_body",
    "NotFoundErrorBody": ".not_found_error_body",
    "ReportEnvelope": ".report_envelope",
    "ReportEnvelopeMeter": ".report_envelope_meter",
    "ReportEnvelopeReport": ".report_envelope_report",
    "ReportEnvelopeReportVolumeItem": ".report_envelope_report_volume_item",
    "ReportEnvelopeSystem": ".report_envelope_system",
    "ServiceUnavailableErrorBody": ".service_unavailable_error_body",
    "Settings": ".settings",
    "SettingsServices": ".settings_services",
    "SettingsServicesBerry": ".settings_services_berry",
    "SettingsServicesCloud": ".settings_services_cloud",
    "SettingsServicesLocal": ".settings_services_local",
    "SettingsServicesModbus": ".settings_services_modbus",
    "SettingsServicesSd": ".settings_services_sd",
    "SettingsSystem": ".settings_system",
    "SystemInfo": ".system_info",
    "SystemInfoDevice": ".system_info_device",
    "SystemInfoMeter": ".system_info_meter",
    "SystemInfoWifi": ".system_info_wifi",
    "TooManyRequestsErrorBody": ".too_many_requests_error_body",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "UnsupportedMediaTypeErrorBody": ".unsupported_media_type_error_body",
    "WiFiNetwork": ".wi_fi_network",
    "WiFiStaSettings": ".wi_fi_sta_settings",
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
    "ActionStatus",
    "ActionsDefinition",
    "ActionsDefinitionActionsItem",
    "ActionsDefinitionActionsItemRequestsItem",
    "ActionsDefinitionActionsItemRequestsItemHttp",
    "ActionsDefinitionActionsItemRequestsItemHttpMethod",
    "ActionsDefinitionActionsItemRequestsItemModbus",
    "ActionsDefinitionActionsItemRequestsItemModbusType",
    "ActionsDefinitionConstValue",
    "BadRequestErrorBody",
    "ConflictErrorBody",
    "ContentTooLargeErrorBody",
    "DirectoryEntry",
    "DirectoryEntryType",
    "DirectoryListing",
    "DirectoryListingFilesItem",
    "DirectoryListingFilesItemType",
    "Error",
    "EthernetSettings",
    "InternalServerErrorBody",
    "NotFoundErrorBody",
    "ReportEnvelope",
    "ReportEnvelopeMeter",
    "ReportEnvelopeReport",
    "ReportEnvelopeReportVolumeItem",
    "ReportEnvelopeSystem",
    "ServiceUnavailableErrorBody",
    "Settings",
    "SettingsServices",
    "SettingsServicesBerry",
    "SettingsServicesCloud",
    "SettingsServicesLocal",
    "SettingsServicesModbus",
    "SettingsServicesSd",
    "SettingsSystem",
    "SystemInfo",
    "SystemInfoDevice",
    "SystemInfoMeter",
    "SystemInfoWifi",
    "TooManyRequestsErrorBody",
    "UnauthorizedErrorBody",
    "UnsupportedMediaTypeErrorBody",
    "WiFiNetwork",
    "WiFiStaSettings",
]
