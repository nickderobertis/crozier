



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .base_meta import BaseMeta
    from .boot_mode import BootMode
    from .callbacks_mapping import CallbacksMapping
    from .compose_spec_label_dict import ComposeSpecLabelDict
    from .computation_get import ComputationGet
    from .container_state import ContainerState
    from .delayed_exception_handler import DelayedExceptionHandler
    from .dns_resolver import DnsResolver
    from .dns_resolver_port import DnsResolverPort
    from .docker_container_inspect import DockerContainerInspect
    from .dynamic_sidecar import DynamicSidecar
    from .dynamic_sidecar_status import DynamicSidecarStatus
    from .encrypted_root_key_str import EncryptedRootKeyStr
    from .error_dict import ErrorDict
    from .error_dict_loc_item import ErrorDictLocItem
    from .file_id_str import FileIdStr
    from .get_project_inactivity_response import GetProjectInactivityResponse
    from .get_task_result_task_task_id_result_get_response import GetTaskResultTaskTaskIdResultGetResponse
    from .group_id_int import GroupIdInt
    from .hardware_info import HardwareInfo
    from .health import Health
    from .healthcheck_result import HealthcheckResult
    from .http_validation_error import HttpValidationError
    from .image_resources import ImageResources
    from .job_encryption_context_metadata import JobEncryptionContextMetadata
    from .legacy_state import LegacyState
    from .models_library_generated_models_docker_rest_api_status import ModelsLibraryGeneratedModelsDockerRestApiStatus
    from .nat_rule import NatRule
    from .nat_rule_tcp_ports_item import NatRuleTcpPortsItem
    from .node_share_state import NodeShareState
    from .node_share_status import NodeShareStatus
    from .node_state import NodeState
    from .output_name import OutputName
    from .path_mappings_label import PathMappingsLabel
    from .pipeline_details import PipelineDetails
    from .port_range import PortRange
    from .port_range_lower import PortRangeLower
    from .port_range_upper import PortRangeUpper
    from .pricing_info import PricingInfo
    from .resource_value import ResourceValue
    from .resource_value_limit import ResourceValueLimit
    from .resource_value_reservation import ResourceValueReservation
    from .restart_policy import RestartPolicy
    from .retrieve_data_out import RetrieveDataOut
    from .retrieve_data_out_enveloped import RetrieveDataOutEnveloped
    from .running_dynamic_service_details import RunningDynamicServiceDetails
    from .running_state import RunningState
    from .scheduler_data import SchedulerData
    from .service_boot_type import ServiceBootType
    from .service_removal_state import ServiceRemovalState
    from .service_state import ServiceState
    from .services_instrumentation import ServicesInstrumentation
    from .simcore_service_director_v2models_dynamic_services_scheduler_status import (
        SimcoreServiceDirectorV2ModelsDynamicServicesSchedulerStatus,
    )
    from .status1 import Status1
    from .task_get import TaskGet
    from .task_log_file_get import TaskLogFileGet
    from .task_progress import TaskProgress
    from .task_result import TaskResult
    from .task_status import TaskStatus
    from .tasks_outputs import TasksOutputs
    from .user_id_int import UserIdInt
    from .user_preferences_version_source import UserPreferencesVersionSource
    from .user_service_command import UserServiceCommand
    from .user_service_command_command import UserServiceCommandCommand
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
    from .wallet_id_int import WalletIdInt
    from .wallet_info_input import WalletInfoInput
    from .wallet_info_input_wallet_credit_amount import WalletInfoInputWalletCreditAmount
    from .wallet_info_output import WalletInfoOutput
_dynamic_imports: typing.Dict[str, str] = {
    "BaseMeta": ".base_meta",
    "BootMode": ".boot_mode",
    "CallbacksMapping": ".callbacks_mapping",
    "ComposeSpecLabelDict": ".compose_spec_label_dict",
    "ComputationGet": ".computation_get",
    "ContainerState": ".container_state",
    "DelayedExceptionHandler": ".delayed_exception_handler",
    "DnsResolver": ".dns_resolver",
    "DnsResolverPort": ".dns_resolver_port",
    "DockerContainerInspect": ".docker_container_inspect",
    "DynamicSidecar": ".dynamic_sidecar",
    "DynamicSidecarStatus": ".dynamic_sidecar_status",
    "EncryptedRootKeyStr": ".encrypted_root_key_str",
    "ErrorDict": ".error_dict",
    "ErrorDictLocItem": ".error_dict_loc_item",
    "FileIdStr": ".file_id_str",
    "GetProjectInactivityResponse": ".get_project_inactivity_response",
    "GetTaskResultTaskTaskIdResultGetResponse": ".get_task_result_task_task_id_result_get_response",
    "GroupIdInt": ".group_id_int",
    "HardwareInfo": ".hardware_info",
    "Health": ".health",
    "HealthcheckResult": ".healthcheck_result",
    "HttpValidationError": ".http_validation_error",
    "ImageResources": ".image_resources",
    "JobEncryptionContextMetadata": ".job_encryption_context_metadata",
    "LegacyState": ".legacy_state",
    "ModelsLibraryGeneratedModelsDockerRestApiStatus": ".models_library_generated_models_docker_rest_api_status",
    "NatRule": ".nat_rule",
    "NatRuleTcpPortsItem": ".nat_rule_tcp_ports_item",
    "NodeShareState": ".node_share_state",
    "NodeShareStatus": ".node_share_status",
    "NodeState": ".node_state",
    "OutputName": ".output_name",
    "PathMappingsLabel": ".path_mappings_label",
    "PipelineDetails": ".pipeline_details",
    "PortRange": ".port_range",
    "PortRangeLower": ".port_range_lower",
    "PortRangeUpper": ".port_range_upper",
    "PricingInfo": ".pricing_info",
    "ResourceValue": ".resource_value",
    "ResourceValueLimit": ".resource_value_limit",
    "ResourceValueReservation": ".resource_value_reservation",
    "RestartPolicy": ".restart_policy",
    "RetrieveDataOut": ".retrieve_data_out",
    "RetrieveDataOutEnveloped": ".retrieve_data_out_enveloped",
    "RunningDynamicServiceDetails": ".running_dynamic_service_details",
    "RunningState": ".running_state",
    "SchedulerData": ".scheduler_data",
    "ServiceBootType": ".service_boot_type",
    "ServiceRemovalState": ".service_removal_state",
    "ServiceState": ".service_state",
    "ServicesInstrumentation": ".services_instrumentation",
    "SimcoreServiceDirectorV2ModelsDynamicServicesSchedulerStatus": ".simcore_service_director_v2models_dynamic_services_scheduler_status",
    "Status1": ".status1",
    "TaskGet": ".task_get",
    "TaskLogFileGet": ".task_log_file_get",
    "TaskProgress": ".task_progress",
    "TaskResult": ".task_result",
    "TaskStatus": ".task_status",
    "TasksOutputs": ".tasks_outputs",
    "UserIdInt": ".user_id_int",
    "UserPreferencesVersionSource": ".user_preferences_version_source",
    "UserServiceCommand": ".user_service_command",
    "UserServiceCommandCommand": ".user_service_command_command",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
    "WalletIdInt": ".wallet_id_int",
    "WalletInfoInput": ".wallet_info_input",
    "WalletInfoInputWalletCreditAmount": ".wallet_info_input_wallet_credit_amount",
    "WalletInfoOutput": ".wallet_info_output",
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
    "BaseMeta",
    "BootMode",
    "CallbacksMapping",
    "ComposeSpecLabelDict",
    "ComputationGet",
    "ContainerState",
    "DelayedExceptionHandler",
    "DnsResolver",
    "DnsResolverPort",
    "DockerContainerInspect",
    "DynamicSidecar",
    "DynamicSidecarStatus",
    "EncryptedRootKeyStr",
    "ErrorDict",
    "ErrorDictLocItem",
    "FileIdStr",
    "GetProjectInactivityResponse",
    "GetTaskResultTaskTaskIdResultGetResponse",
    "GroupIdInt",
    "HardwareInfo",
    "Health",
    "HealthcheckResult",
    "HttpValidationError",
    "ImageResources",
    "JobEncryptionContextMetadata",
    "LegacyState",
    "ModelsLibraryGeneratedModelsDockerRestApiStatus",
    "NatRule",
    "NatRuleTcpPortsItem",
    "NodeShareState",
    "NodeShareStatus",
    "NodeState",
    "OutputName",
    "PathMappingsLabel",
    "PipelineDetails",
    "PortRange",
    "PortRangeLower",
    "PortRangeUpper",
    "PricingInfo",
    "ResourceValue",
    "ResourceValueLimit",
    "ResourceValueReservation",
    "RestartPolicy",
    "RetrieveDataOut",
    "RetrieveDataOutEnveloped",
    "RunningDynamicServiceDetails",
    "RunningState",
    "SchedulerData",
    "ServiceBootType",
    "ServiceRemovalState",
    "ServiceState",
    "ServicesInstrumentation",
    "SimcoreServiceDirectorV2ModelsDynamicServicesSchedulerStatus",
    "Status1",
    "TaskGet",
    "TaskLogFileGet",
    "TaskProgress",
    "TaskResult",
    "TaskStatus",
    "TasksOutputs",
    "UserIdInt",
    "UserPreferencesVersionSource",
    "UserServiceCommand",
    "UserServiceCommandCommand",
    "ValidationError",
    "ValidationErrorLocItem",
    "WalletIdInt",
    "WalletInfoInput",
    "WalletInfoInputWalletCreditAmount",
    "WalletInfoOutput",
]
