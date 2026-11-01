



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account_credential_details import AccountCredentialDetails
    from .account_credential_details_data_destination_type import AccountCredentialDetailsDataDestinationType
    from .address_validation_output import AddressValidationOutput
    from .address_validation_properties import AddressValidationProperties
    from .address_validation_properties_validation_status import AddressValidationPropertiesValidationStatus
    from .appliance_network_configuration import ApplianceNetworkConfiguration
    from .arm_base_object import ArmBaseObject
    from .available_sku_request import AvailableSkuRequest
    from .available_sku_request_sku_names_item import AvailableSkuRequestSkuNamesItem
    from .available_sku_request_transfer_type import AvailableSkuRequestTransferType
    from .available_skus_result import AvailableSkusResult
    from .cloud_error import CloudError
    from .contact_details import ContactDetails
    from .copy_log_details import CopyLogDetails
    from .copy_log_details_copy_log_details_type import CopyLogDetailsCopyLogDetailsType
    from .copy_progress import CopyProgress
    from .copy_progress_data_destination_type import CopyProgressDataDestinationType
    from .create_job_validations import CreateJobValidations
    from .create_order_limit_for_subscription_validation_request import CreateOrderLimitForSubscriptionValidationRequest
    from .create_order_limit_for_subscription_validation_request_device_type import (
        CreateOrderLimitForSubscriptionValidationRequestDeviceType,
    )
    from .create_order_limit_for_subscription_validation_response_properties import (
        CreateOrderLimitForSubscriptionValidationResponseProperties,
    )
    from .create_order_limit_for_subscription_validation_response_properties_status import (
        CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus,
    )
    from .data_box_account_copy_log_details import DataBoxAccountCopyLogDetails
    from .data_box_disk_copy_log_details import DataBoxDiskCopyLogDetails
    from .data_box_disk_copy_progress import DataBoxDiskCopyProgress
    from .data_box_disk_copy_progress_status import DataBoxDiskCopyProgressStatus
    from .data_box_disk_job_details import DataBoxDiskJobDetails
    from .data_box_disk_job_secrets import DataBoxDiskJobSecrets
    from .data_box_heavy_account_copy_log_details import DataBoxHeavyAccountCopyLogDetails
    from .data_box_heavy_job_details import DataBoxHeavyJobDetails
    from .data_box_heavy_job_secrets import DataBoxHeavyJobSecrets
    from .data_box_heavy_secret import DataBoxHeavySecret
    from .data_box_job_details import DataBoxJobDetails
    from .data_box_schedule_availability_request import DataBoxScheduleAvailabilityRequest
    from .data_box_secret import DataBoxSecret
    from .data_destination_details_validation_request import DataDestinationDetailsValidationRequest
    from .data_destination_details_validation_response_properties import (
        DataDestinationDetailsValidationResponseProperties,
    )
    from .data_destination_details_validation_response_properties_status import (
        DataDestinationDetailsValidationResponsePropertiesStatus,
    )
    from .databox_job_secrets import DataboxJobSecrets
    from .dc_access_security_code import DcAccessSecurityCode
    from .destination_account_details import DestinationAccountDetails
    from .destination_account_details_data_destination_type import DestinationAccountDetailsDataDestinationType
    from .destination_managed_disk_details import DestinationManagedDiskDetails
    from .destination_storage_account_details import DestinationStorageAccountDetails
    from .destination_to_service_location_map import DestinationToServiceLocationMap
    from .disk_schedule_availability_request import DiskScheduleAvailabilityRequest
    from .disk_secret import DiskSecret
    from .error import Error
    from .heavy_schedule_availability_request import HeavyScheduleAvailabilityRequest
    from .job_delivery_info import JobDeliveryInfo
    from .job_details import JobDetails
    from .job_details_job_details_type import JobDetailsJobDetailsType
    from .job_error_details import JobErrorDetails
    from .job_properties import JobProperties
    from .job_properties_delivery_type import JobPropertiesDeliveryType
    from .job_properties_status import JobPropertiesStatus
    from .job_resource import JobResource
    from .job_resource_list import JobResourceList
    from .job_secrets import JobSecrets
    from .job_secrets_job_secrets_type import JobSecretsJobSecretsType
    from .job_stages import JobStages
    from .job_stages_stage_name import JobStagesStageName
    from .job_stages_stage_status import JobStagesStageStatus
    from .notification_preference import NotificationPreference
    from .notification_preference_stage_name import NotificationPreferenceStageName
    from .oauth_scope import OauthScope
    from .operation import Operation
    from .operation_display import OperationDisplay
    from .operation_list import OperationList
    from .operation_properties import OperationProperties
    from .package_shipping_details import PackageShippingDetails
    from .preferences import Preferences
    from .preferences_validation_request import PreferencesValidationRequest
    from .preferences_validation_request_device_type import PreferencesValidationRequestDeviceType
    from .preferences_validation_response_properties import PreferencesValidationResponseProperties
    from .preferences_validation_response_properties_status import PreferencesValidationResponsePropertiesStatus
    from .region_configuration_response import RegionConfigurationResponse
    from .resource import Resource
    from .schedule_availability_request import ScheduleAvailabilityRequest
    from .schedule_availability_request_sku_name import ScheduleAvailabilityRequestSkuName
    from .schedule_availability_response import ScheduleAvailabilityResponse
    from .share_credential_details import ShareCredentialDetails
    from .share_credential_details_share_type import ShareCredentialDetailsShareType
    from .share_credential_details_supported_access_protocols_item import (
        ShareCredentialDetailsSupportedAccessProtocolsItem,
    )
    from .shipment_pick_up_response import ShipmentPickUpResponse
    from .shipping_address import ShippingAddress
    from .shipping_address_address_type import ShippingAddressAddressType
    from .sku import Sku
    from .sku_availability_validation_request import SkuAvailabilityValidationRequest
    from .sku_availability_validation_request_device_type import SkuAvailabilityValidationRequestDeviceType
    from .sku_availability_validation_request_transfer_type import SkuAvailabilityValidationRequestTransferType
    from .sku_availability_validation_response_properties import SkuAvailabilityValidationResponseProperties
    from .sku_availability_validation_response_properties_status import (
        SkuAvailabilityValidationResponsePropertiesStatus,
    )
    from .sku_capacity import SkuCapacity
    from .sku_cost import SkuCost
    from .sku_information import SkuInformation
    from .sku_name import SkuName
    from .sku_properties import SkuProperties
    from .sku_properties_disabled_reason import SkuPropertiesDisabledReason
    from .subscription_is_allowed_to_create_job_validation_request import (
        SubscriptionIsAllowedToCreateJobValidationRequest,
    )
    from .subscription_is_allowed_to_create_job_validation_response_properties import (
        SubscriptionIsAllowedToCreateJobValidationResponseProperties,
    )
    from .subscription_is_allowed_to_create_job_validation_response_properties_status import (
        SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus,
    )
    from .transport_availability_details import TransportAvailabilityDetails
    from .transport_availability_details_shipment_type import TransportAvailabilityDetailsShipmentType
    from .transport_availability_request import TransportAvailabilityRequest
    from .transport_availability_request_sku_name import TransportAvailabilityRequestSkuName
    from .transport_availability_response import TransportAvailabilityResponse
    from .transport_preferences import TransportPreferences
    from .transport_preferences_preferred_shipment_type import TransportPreferencesPreferredShipmentType
    from .unencrypted_credentials import UnencryptedCredentials
    from .unencrypted_credentials_list import UnencryptedCredentialsList
    from .update_job_details import UpdateJobDetails
    from .update_job_properties import UpdateJobProperties
    from .validation_input_request import ValidationInputRequest
    from .validation_input_request_validation_type import ValidationInputRequestValidationType
    from .validation_input_response import ValidationInputResponse
    from .validation_input_response_validation_type import ValidationInputResponseValidationType
    from .validation_request import ValidationRequest
    from .validation_request_validation_category import ValidationRequestValidationCategory
    from .validation_response import ValidationResponse
    from .validation_response_properties import ValidationResponseProperties
    from .validation_response_properties_status import ValidationResponsePropertiesStatus
_dynamic_imports: typing.Dict[str, str] = {
    "AccountCredentialDetails": ".account_credential_details",
    "AccountCredentialDetailsDataDestinationType": ".account_credential_details_data_destination_type",
    "AddressValidationOutput": ".address_validation_output",
    "AddressValidationProperties": ".address_validation_properties",
    "AddressValidationPropertiesValidationStatus": ".address_validation_properties_validation_status",
    "ApplianceNetworkConfiguration": ".appliance_network_configuration",
    "ArmBaseObject": ".arm_base_object",
    "AvailableSkuRequest": ".available_sku_request",
    "AvailableSkuRequestSkuNamesItem": ".available_sku_request_sku_names_item",
    "AvailableSkuRequestTransferType": ".available_sku_request_transfer_type",
    "AvailableSkusResult": ".available_skus_result",
    "CloudError": ".cloud_error",
    "ContactDetails": ".contact_details",
    "CopyLogDetails": ".copy_log_details",
    "CopyLogDetailsCopyLogDetailsType": ".copy_log_details_copy_log_details_type",
    "CopyProgress": ".copy_progress",
    "CopyProgressDataDestinationType": ".copy_progress_data_destination_type",
    "CreateJobValidations": ".create_job_validations",
    "CreateOrderLimitForSubscriptionValidationRequest": ".create_order_limit_for_subscription_validation_request",
    "CreateOrderLimitForSubscriptionValidationRequestDeviceType": ".create_order_limit_for_subscription_validation_request_device_type",
    "CreateOrderLimitForSubscriptionValidationResponseProperties": ".create_order_limit_for_subscription_validation_response_properties",
    "CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus": ".create_order_limit_for_subscription_validation_response_properties_status",
    "DataBoxAccountCopyLogDetails": ".data_box_account_copy_log_details",
    "DataBoxDiskCopyLogDetails": ".data_box_disk_copy_log_details",
    "DataBoxDiskCopyProgress": ".data_box_disk_copy_progress",
    "DataBoxDiskCopyProgressStatus": ".data_box_disk_copy_progress_status",
    "DataBoxDiskJobDetails": ".data_box_disk_job_details",
    "DataBoxDiskJobSecrets": ".data_box_disk_job_secrets",
    "DataBoxHeavyAccountCopyLogDetails": ".data_box_heavy_account_copy_log_details",
    "DataBoxHeavyJobDetails": ".data_box_heavy_job_details",
    "DataBoxHeavyJobSecrets": ".data_box_heavy_job_secrets",
    "DataBoxHeavySecret": ".data_box_heavy_secret",
    "DataBoxJobDetails": ".data_box_job_details",
    "DataBoxScheduleAvailabilityRequest": ".data_box_schedule_availability_request",
    "DataBoxSecret": ".data_box_secret",
    "DataDestinationDetailsValidationRequest": ".data_destination_details_validation_request",
    "DataDestinationDetailsValidationResponseProperties": ".data_destination_details_validation_response_properties",
    "DataDestinationDetailsValidationResponsePropertiesStatus": ".data_destination_details_validation_response_properties_status",
    "DataboxJobSecrets": ".databox_job_secrets",
    "DcAccessSecurityCode": ".dc_access_security_code",
    "DestinationAccountDetails": ".destination_account_details",
    "DestinationAccountDetailsDataDestinationType": ".destination_account_details_data_destination_type",
    "DestinationManagedDiskDetails": ".destination_managed_disk_details",
    "DestinationStorageAccountDetails": ".destination_storage_account_details",
    "DestinationToServiceLocationMap": ".destination_to_service_location_map",
    "DiskScheduleAvailabilityRequest": ".disk_schedule_availability_request",
    "DiskSecret": ".disk_secret",
    "Error": ".error",
    "HeavyScheduleAvailabilityRequest": ".heavy_schedule_availability_request",
    "JobDeliveryInfo": ".job_delivery_info",
    "JobDetails": ".job_details",
    "JobDetailsJobDetailsType": ".job_details_job_details_type",
    "JobErrorDetails": ".job_error_details",
    "JobProperties": ".job_properties",
    "JobPropertiesDeliveryType": ".job_properties_delivery_type",
    "JobPropertiesStatus": ".job_properties_status",
    "JobResource": ".job_resource",
    "JobResourceList": ".job_resource_list",
    "JobSecrets": ".job_secrets",
    "JobSecretsJobSecretsType": ".job_secrets_job_secrets_type",
    "JobStages": ".job_stages",
    "JobStagesStageName": ".job_stages_stage_name",
    "JobStagesStageStatus": ".job_stages_stage_status",
    "NotificationPreference": ".notification_preference",
    "NotificationPreferenceStageName": ".notification_preference_stage_name",
    "OauthScope": ".oauth_scope",
    "Operation": ".operation",
    "OperationDisplay": ".operation_display",
    "OperationList": ".operation_list",
    "OperationProperties": ".operation_properties",
    "PackageShippingDetails": ".package_shipping_details",
    "Preferences": ".preferences",
    "PreferencesValidationRequest": ".preferences_validation_request",
    "PreferencesValidationRequestDeviceType": ".preferences_validation_request_device_type",
    "PreferencesValidationResponseProperties": ".preferences_validation_response_properties",
    "PreferencesValidationResponsePropertiesStatus": ".preferences_validation_response_properties_status",
    "RegionConfigurationResponse": ".region_configuration_response",
    "Resource": ".resource",
    "ScheduleAvailabilityRequest": ".schedule_availability_request",
    "ScheduleAvailabilityRequestSkuName": ".schedule_availability_request_sku_name",
    "ScheduleAvailabilityResponse": ".schedule_availability_response",
    "ShareCredentialDetails": ".share_credential_details",
    "ShareCredentialDetailsShareType": ".share_credential_details_share_type",
    "ShareCredentialDetailsSupportedAccessProtocolsItem": ".share_credential_details_supported_access_protocols_item",
    "ShipmentPickUpResponse": ".shipment_pick_up_response",
    "ShippingAddress": ".shipping_address",
    "ShippingAddressAddressType": ".shipping_address_address_type",
    "Sku": ".sku",
    "SkuAvailabilityValidationRequest": ".sku_availability_validation_request",
    "SkuAvailabilityValidationRequestDeviceType": ".sku_availability_validation_request_device_type",
    "SkuAvailabilityValidationRequestTransferType": ".sku_availability_validation_request_transfer_type",
    "SkuAvailabilityValidationResponseProperties": ".sku_availability_validation_response_properties",
    "SkuAvailabilityValidationResponsePropertiesStatus": ".sku_availability_validation_response_properties_status",
    "SkuCapacity": ".sku_capacity",
    "SkuCost": ".sku_cost",
    "SkuInformation": ".sku_information",
    "SkuName": ".sku_name",
    "SkuProperties": ".sku_properties",
    "SkuPropertiesDisabledReason": ".sku_properties_disabled_reason",
    "SubscriptionIsAllowedToCreateJobValidationRequest": ".subscription_is_allowed_to_create_job_validation_request",
    "SubscriptionIsAllowedToCreateJobValidationResponseProperties": ".subscription_is_allowed_to_create_job_validation_response_properties",
    "SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus": ".subscription_is_allowed_to_create_job_validation_response_properties_status",
    "TransportAvailabilityDetails": ".transport_availability_details",
    "TransportAvailabilityDetailsShipmentType": ".transport_availability_details_shipment_type",
    "TransportAvailabilityRequest": ".transport_availability_request",
    "TransportAvailabilityRequestSkuName": ".transport_availability_request_sku_name",
    "TransportAvailabilityResponse": ".transport_availability_response",
    "TransportPreferences": ".transport_preferences",
    "TransportPreferencesPreferredShipmentType": ".transport_preferences_preferred_shipment_type",
    "UnencryptedCredentials": ".unencrypted_credentials",
    "UnencryptedCredentialsList": ".unencrypted_credentials_list",
    "UpdateJobDetails": ".update_job_details",
    "UpdateJobProperties": ".update_job_properties",
    "ValidationInputRequest": ".validation_input_request",
    "ValidationInputRequestValidationType": ".validation_input_request_validation_type",
    "ValidationInputResponse": ".validation_input_response",
    "ValidationInputResponseValidationType": ".validation_input_response_validation_type",
    "ValidationRequest": ".validation_request",
    "ValidationRequestValidationCategory": ".validation_request_validation_category",
    "ValidationResponse": ".validation_response",
    "ValidationResponseProperties": ".validation_response_properties",
    "ValidationResponsePropertiesStatus": ".validation_response_properties_status",
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
    "AccountCredentialDetails",
    "AccountCredentialDetailsDataDestinationType",
    "AddressValidationOutput",
    "AddressValidationProperties",
    "AddressValidationPropertiesValidationStatus",
    "ApplianceNetworkConfiguration",
    "ArmBaseObject",
    "AvailableSkuRequest",
    "AvailableSkuRequestSkuNamesItem",
    "AvailableSkuRequestTransferType",
    "AvailableSkusResult",
    "CloudError",
    "ContactDetails",
    "CopyLogDetails",
    "CopyLogDetailsCopyLogDetailsType",
    "CopyProgress",
    "CopyProgressDataDestinationType",
    "CreateJobValidations",
    "CreateOrderLimitForSubscriptionValidationRequest",
    "CreateOrderLimitForSubscriptionValidationRequestDeviceType",
    "CreateOrderLimitForSubscriptionValidationResponseProperties",
    "CreateOrderLimitForSubscriptionValidationResponsePropertiesStatus",
    "DataBoxAccountCopyLogDetails",
    "DataBoxDiskCopyLogDetails",
    "DataBoxDiskCopyProgress",
    "DataBoxDiskCopyProgressStatus",
    "DataBoxDiskJobDetails",
    "DataBoxDiskJobSecrets",
    "DataBoxHeavyAccountCopyLogDetails",
    "DataBoxHeavyJobDetails",
    "DataBoxHeavyJobSecrets",
    "DataBoxHeavySecret",
    "DataBoxJobDetails",
    "DataBoxScheduleAvailabilityRequest",
    "DataBoxSecret",
    "DataDestinationDetailsValidationRequest",
    "DataDestinationDetailsValidationResponseProperties",
    "DataDestinationDetailsValidationResponsePropertiesStatus",
    "DataboxJobSecrets",
    "DcAccessSecurityCode",
    "DestinationAccountDetails",
    "DestinationAccountDetailsDataDestinationType",
    "DestinationManagedDiskDetails",
    "DestinationStorageAccountDetails",
    "DestinationToServiceLocationMap",
    "DiskScheduleAvailabilityRequest",
    "DiskSecret",
    "Error",
    "HeavyScheduleAvailabilityRequest",
    "JobDeliveryInfo",
    "JobDetails",
    "JobDetailsJobDetailsType",
    "JobErrorDetails",
    "JobProperties",
    "JobPropertiesDeliveryType",
    "JobPropertiesStatus",
    "JobResource",
    "JobResourceList",
    "JobSecrets",
    "JobSecretsJobSecretsType",
    "JobStages",
    "JobStagesStageName",
    "JobStagesStageStatus",
    "NotificationPreference",
    "NotificationPreferenceStageName",
    "OauthScope",
    "Operation",
    "OperationDisplay",
    "OperationList",
    "OperationProperties",
    "PackageShippingDetails",
    "Preferences",
    "PreferencesValidationRequest",
    "PreferencesValidationRequestDeviceType",
    "PreferencesValidationResponseProperties",
    "PreferencesValidationResponsePropertiesStatus",
    "RegionConfigurationResponse",
    "Resource",
    "ScheduleAvailabilityRequest",
    "ScheduleAvailabilityRequestSkuName",
    "ScheduleAvailabilityResponse",
    "ShareCredentialDetails",
    "ShareCredentialDetailsShareType",
    "ShareCredentialDetailsSupportedAccessProtocolsItem",
    "ShipmentPickUpResponse",
    "ShippingAddress",
    "ShippingAddressAddressType",
    "Sku",
    "SkuAvailabilityValidationRequest",
    "SkuAvailabilityValidationRequestDeviceType",
    "SkuAvailabilityValidationRequestTransferType",
    "SkuAvailabilityValidationResponseProperties",
    "SkuAvailabilityValidationResponsePropertiesStatus",
    "SkuCapacity",
    "SkuCost",
    "SkuInformation",
    "SkuName",
    "SkuProperties",
    "SkuPropertiesDisabledReason",
    "SubscriptionIsAllowedToCreateJobValidationRequest",
    "SubscriptionIsAllowedToCreateJobValidationResponseProperties",
    "SubscriptionIsAllowedToCreateJobValidationResponsePropertiesStatus",
    "TransportAvailabilityDetails",
    "TransportAvailabilityDetailsShipmentType",
    "TransportAvailabilityRequest",
    "TransportAvailabilityRequestSkuName",
    "TransportAvailabilityResponse",
    "TransportPreferences",
    "TransportPreferencesPreferredShipmentType",
    "UnencryptedCredentials",
    "UnencryptedCredentialsList",
    "UpdateJobDetails",
    "UpdateJobProperties",
    "ValidationInputRequest",
    "ValidationInputRequestValidationType",
    "ValidationInputResponse",
    "ValidationInputResponseValidationType",
    "ValidationRequest",
    "ValidationRequestValidationCategory",
    "ValidationResponse",
    "ValidationResponseProperties",
    "ValidationResponsePropertiesStatus",
]
