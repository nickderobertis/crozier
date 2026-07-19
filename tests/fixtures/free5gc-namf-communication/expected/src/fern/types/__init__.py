



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_type import AccessType
    from .allowed_nssai import AllowedNssai
    from .allowed_snssai import AllowedSnssai
    from .am_policy_req_trigger import AmPolicyReqTrigger
    from .ambr import Ambr
    from .amf_event import AmfEvent
    from .amf_event_area import AmfEventArea
    from .amf_event_mode import AmfEventMode
    from .amf_event_subscription import AmfEventSubscription
    from .amf_event_trigger import AmfEventTrigger
    from .amf_event_type import AmfEventType
    from .amf_id import AmfId
    from .amf_name import AmfName
    from .amf_status_change_notification import AmfStatusChangeNotification
    from .amf_status_info import AmfStatusInfo
    from .area import Area
    from .area_code import AreaCode
    from .area_of_validity import AreaOfValidity
    from .arp import Arp
    from .arp_priority_level import ArpPriorityLevel
    from .assign_ebi_error import AssignEbiError
    from .assign_ebi_failed import AssignEbiFailed
    from .assigned_ebi_data import AssignedEbiData
    from .bit_rate import BitRate
    from .bytes import Bytes
    from .ciphering_algorithm import CipheringAlgorithm
    from .configured_snssai import ConfiguredSnssai
    from .core_network_type import CoreNetworkType
    from .correlation_id import CorrelationId
    from .create_ue_context_response201 import CreateUeContextResponse201
    from .date_time import DateTime
    from .dnn import Dnn
    from .drx_parameter import DrxParameter
    from .ebi_arp_mapping import EbiArpMapping
    from .ecgi import Ecgi
    from .eps_bearer_id import EpsBearerId
    from .eps_bearer_id2 import EpsBearerId2
    from .eutra_cell_id import EutraCellId
    from .eutra_location import EutraLocation
    from .expected_ue_behavior import ExpectedUeBehavior
    from .five_g_mm_capability import FiveGMmCapability
    from .five_qi import FiveQi
    from .g_nb_id import GNbId
    from .global_ran_node_id import GlobalRanNodeId
    from .gpsi import Gpsi
    from .group_id import GroupId
    from .guami import Guami
    from .integrity_algorithm import IntegrityAlgorithm
    from .invalid_param import InvalidParam
    from .ipv4addr import Ipv4Addr
    from .ipv6addr import Ipv6Addr
    from .key_amf import KeyAmf
    from .key_amf_type import KeyAmfType
    from .ladn_info import LadnInfo
    from .location_filter import LocationFilter
    from .mcc import Mcc
    from .mm_context import MmContext
    from .mnc import Mnc
    from .n1message_class import N1MessageClass
    from .n1message_container import N1MessageContainer
    from .n1message_notification import N1MessageNotification
    from .n1n2message_transfer_cause import N1N2MessageTransferCause
    from .n1n2message_transfer_error import N1N2MessageTransferError
    from .n1n2message_transfer_req_data import N1N2MessageTransferReqData
    from .n1n2message_transfer_request_body import N1N2MessageTransferRequestBody
    from .n1n2message_transfer_rsp_data import N1N2MessageTransferRspData
    from .n1n2msg_txfr_err_detail import N1N2MsgTxfrErrDetail
    from .n1n2msg_txfr_failure_notification import N1N2MsgTxfrFailureNotification
    from .n2info_container import N2InfoContainer
    from .n2info_content import N2InfoContent
    from .n2info_notify_reason import N2InfoNotifyReason
    from .n2information_class import N2InformationClass
    from .n2information_notification import N2InformationNotification
    from .n2information_transfer_error import N2InformationTransferError
    from .n2information_transfer_req_data import N2InformationTransferReqData
    from .n2information_transfer_result import N2InformationTransferResult
    from .n2information_transfer_rsp_data import N2InformationTransferRspData
    from .n2ran_information import N2RanInformation
    from .n2sm_information import N2SmInformation
    from .n3ga_location import N3GaLocation
    from .n3iwf_id import N3IwfId
    from .nas_count import NasCount
    from .nas_security_mode import NasSecurityMode
    from .ncgi import Ncgi
    from .nf_group_id import NfGroupId
    from .nf_instance_id import NfInstanceId
    from .ng_ap_cause import NgApCause
    from .ng_ksi import NgKsi
    from .ng_ran_target_id import NgRanTargetId
    from .ngap_ie_type import NgapIeType
    from .nge_nb_id import NgeNbId
    from .non_ue_n2info_subscription_created_data import NonUeN2InfoSubscriptionCreatedData
    from .non_ue_n2message_transfer_request_body import NonUeN2MessageTransferRequestBody
    from .nr_cell_id import NrCellId
    from .nr_location import NrLocation
    from .nrppa_information import NrppaInformation
    from .nsi_id import NsiId
    from .nsi_information import NsiInformation
    from .nssai_mapping import NssaiMapping
    from .oauth_scope import OauthScope
    from .omc_identifier import OmcIdentifier
    from .pdu_session_context import PduSessionContext
    from .pdu_session_id import PduSessionId
    from .pei import Pei
    from .plmn_id import PlmnId
    from .ppi import Ppi
    from .preemption_capability import PreemptionCapability
    from .preemption_vulnerability import PreemptionVulnerability
    from .presence_info import PresenceInfo
    from .presence_state import PresenceState
    from .problem_details import ProblemDetails
    from .pws_error_data import PwsErrorData
    from .pws_information import PwsInformation
    from .pws_response_data import PwsResponseData
    from .rat_selector import RatSelector
    from .rat_type import RatType
    from .ref_to_binary_data import RefToBinaryData
    from .registration_context_container import RegistrationContextContainer
    from .restriction_type import RestrictionType
    from .rfsp_index import RfspIndex
    from .s1ue_network_capability import S1UeNetworkCapability
    from .sc_type import ScType
    from .seaf_data import SeafData
    from .service_area_restriction import ServiceAreaRestriction
    from .sms_support import SmsSupport
    from .snssai import Snssai
    from .status_change import StatusChange
    from .subscribed_data_filter import SubscribedDataFilter
    from .subscription_data import SubscriptionData
    from .supi import Supi
    from .supported_features import SupportedFeatures
    from .tac import Tac
    from .tai import Tai
    from .time_zone import TimeZone
    from .trace_data import TraceData
    from .trace_depth import TraceDepth
    from .transfer_reason import TransferReason
    from .ue_context import UeContext
    from .ue_context_create_data import UeContextCreateData
    from .ue_context_create_error import UeContextCreateError
    from .ue_context_created_data import UeContextCreatedData
    from .ue_context_transfer_req_data import UeContextTransferReqData
    from .ue_context_transfer_request_body import UeContextTransferRequestBody
    from .ue_context_transfer_response200 import UeContextTransferResponse200
    from .ue_context_transfer_rsp_data import UeContextTransferRspData
    from .ue_context_transfer_status import UeContextTransferStatus
    from .ue_n1n2info_subscription_created_data import UeN1N2InfoSubscriptionCreatedData
    from .ue_reg_status_update_rsp_data import UeRegStatusUpdateRspData
    from .ue_security_capability import UeSecurityCapability
    from .uint16 import Uint16
    from .uinteger import Uinteger
    from .uri import Uri
    from .user_location import UserLocation
_dynamic_imports: typing.Dict[str, str] = {
    "AccessType": ".access_type",
    "AllowedNssai": ".allowed_nssai",
    "AllowedSnssai": ".allowed_snssai",
    "AmPolicyReqTrigger": ".am_policy_req_trigger",
    "Ambr": ".ambr",
    "AmfEvent": ".amf_event",
    "AmfEventArea": ".amf_event_area",
    "AmfEventMode": ".amf_event_mode",
    "AmfEventSubscription": ".amf_event_subscription",
    "AmfEventTrigger": ".amf_event_trigger",
    "AmfEventType": ".amf_event_type",
    "AmfId": ".amf_id",
    "AmfName": ".amf_name",
    "AmfStatusChangeNotification": ".amf_status_change_notification",
    "AmfStatusInfo": ".amf_status_info",
    "Area": ".area",
    "AreaCode": ".area_code",
    "AreaOfValidity": ".area_of_validity",
    "Arp": ".arp",
    "ArpPriorityLevel": ".arp_priority_level",
    "AssignEbiError": ".assign_ebi_error",
    "AssignEbiFailed": ".assign_ebi_failed",
    "AssignedEbiData": ".assigned_ebi_data",
    "BitRate": ".bit_rate",
    "Bytes": ".bytes",
    "CipheringAlgorithm": ".ciphering_algorithm",
    "ConfiguredSnssai": ".configured_snssai",
    "CoreNetworkType": ".core_network_type",
    "CorrelationId": ".correlation_id",
    "CreateUeContextResponse201": ".create_ue_context_response201",
    "DateTime": ".date_time",
    "Dnn": ".dnn",
    "DrxParameter": ".drx_parameter",
    "EbiArpMapping": ".ebi_arp_mapping",
    "Ecgi": ".ecgi",
    "EpsBearerId": ".eps_bearer_id",
    "EpsBearerId2": ".eps_bearer_id2",
    "EutraCellId": ".eutra_cell_id",
    "EutraLocation": ".eutra_location",
    "ExpectedUeBehavior": ".expected_ue_behavior",
    "FiveGMmCapability": ".five_g_mm_capability",
    "FiveQi": ".five_qi",
    "GNbId": ".g_nb_id",
    "GlobalRanNodeId": ".global_ran_node_id",
    "Gpsi": ".gpsi",
    "GroupId": ".group_id",
    "Guami": ".guami",
    "IntegrityAlgorithm": ".integrity_algorithm",
    "InvalidParam": ".invalid_param",
    "Ipv4Addr": ".ipv4addr",
    "Ipv6Addr": ".ipv6addr",
    "KeyAmf": ".key_amf",
    "KeyAmfType": ".key_amf_type",
    "LadnInfo": ".ladn_info",
    "LocationFilter": ".location_filter",
    "Mcc": ".mcc",
    "MmContext": ".mm_context",
    "Mnc": ".mnc",
    "N1MessageClass": ".n1message_class",
    "N1MessageContainer": ".n1message_container",
    "N1MessageNotification": ".n1message_notification",
    "N1N2MessageTransferCause": ".n1n2message_transfer_cause",
    "N1N2MessageTransferError": ".n1n2message_transfer_error",
    "N1N2MessageTransferReqData": ".n1n2message_transfer_req_data",
    "N1N2MessageTransferRequestBody": ".n1n2message_transfer_request_body",
    "N1N2MessageTransferRspData": ".n1n2message_transfer_rsp_data",
    "N1N2MsgTxfrErrDetail": ".n1n2msg_txfr_err_detail",
    "N1N2MsgTxfrFailureNotification": ".n1n2msg_txfr_failure_notification",
    "N2InfoContainer": ".n2info_container",
    "N2InfoContent": ".n2info_content",
    "N2InfoNotifyReason": ".n2info_notify_reason",
    "N2InformationClass": ".n2information_class",
    "N2InformationNotification": ".n2information_notification",
    "N2InformationTransferError": ".n2information_transfer_error",
    "N2InformationTransferReqData": ".n2information_transfer_req_data",
    "N2InformationTransferResult": ".n2information_transfer_result",
    "N2InformationTransferRspData": ".n2information_transfer_rsp_data",
    "N2RanInformation": ".n2ran_information",
    "N2SmInformation": ".n2sm_information",
    "N3GaLocation": ".n3ga_location",
    "N3IwfId": ".n3iwf_id",
    "NasCount": ".nas_count",
    "NasSecurityMode": ".nas_security_mode",
    "Ncgi": ".ncgi",
    "NfGroupId": ".nf_group_id",
    "NfInstanceId": ".nf_instance_id",
    "NgApCause": ".ng_ap_cause",
    "NgKsi": ".ng_ksi",
    "NgRanTargetId": ".ng_ran_target_id",
    "NgapIeType": ".ngap_ie_type",
    "NgeNbId": ".nge_nb_id",
    "NonUeN2InfoSubscriptionCreatedData": ".non_ue_n2info_subscription_created_data",
    "NonUeN2MessageTransferRequestBody": ".non_ue_n2message_transfer_request_body",
    "NrCellId": ".nr_cell_id",
    "NrLocation": ".nr_location",
    "NrppaInformation": ".nrppa_information",
    "NsiId": ".nsi_id",
    "NsiInformation": ".nsi_information",
    "NssaiMapping": ".nssai_mapping",
    "OauthScope": ".oauth_scope",
    "OmcIdentifier": ".omc_identifier",
    "PduSessionContext": ".pdu_session_context",
    "PduSessionId": ".pdu_session_id",
    "Pei": ".pei",
    "PlmnId": ".plmn_id",
    "Ppi": ".ppi",
    "PreemptionCapability": ".preemption_capability",
    "PreemptionVulnerability": ".preemption_vulnerability",
    "PresenceInfo": ".presence_info",
    "PresenceState": ".presence_state",
    "ProblemDetails": ".problem_details",
    "PwsErrorData": ".pws_error_data",
    "PwsInformation": ".pws_information",
    "PwsResponseData": ".pws_response_data",
    "RatSelector": ".rat_selector",
    "RatType": ".rat_type",
    "RefToBinaryData": ".ref_to_binary_data",
    "RegistrationContextContainer": ".registration_context_container",
    "RestrictionType": ".restriction_type",
    "RfspIndex": ".rfsp_index",
    "S1UeNetworkCapability": ".s1ue_network_capability",
    "ScType": ".sc_type",
    "SeafData": ".seaf_data",
    "ServiceAreaRestriction": ".service_area_restriction",
    "SmsSupport": ".sms_support",
    "Snssai": ".snssai",
    "StatusChange": ".status_change",
    "SubscribedDataFilter": ".subscribed_data_filter",
    "SubscriptionData": ".subscription_data",
    "Supi": ".supi",
    "SupportedFeatures": ".supported_features",
    "Tac": ".tac",
    "Tai": ".tai",
    "TimeZone": ".time_zone",
    "TraceData": ".trace_data",
    "TraceDepth": ".trace_depth",
    "TransferReason": ".transfer_reason",
    "UeContext": ".ue_context",
    "UeContextCreateData": ".ue_context_create_data",
    "UeContextCreateError": ".ue_context_create_error",
    "UeContextCreatedData": ".ue_context_created_data",
    "UeContextTransferReqData": ".ue_context_transfer_req_data",
    "UeContextTransferRequestBody": ".ue_context_transfer_request_body",
    "UeContextTransferResponse200": ".ue_context_transfer_response200",
    "UeContextTransferRspData": ".ue_context_transfer_rsp_data",
    "UeContextTransferStatus": ".ue_context_transfer_status",
    "UeN1N2InfoSubscriptionCreatedData": ".ue_n1n2info_subscription_created_data",
    "UeRegStatusUpdateRspData": ".ue_reg_status_update_rsp_data",
    "UeSecurityCapability": ".ue_security_capability",
    "Uint16": ".uint16",
    "Uinteger": ".uinteger",
    "Uri": ".uri",
    "UserLocation": ".user_location",
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
    "AccessType",
    "AllowedNssai",
    "AllowedSnssai",
    "AmPolicyReqTrigger",
    "Ambr",
    "AmfEvent",
    "AmfEventArea",
    "AmfEventMode",
    "AmfEventSubscription",
    "AmfEventTrigger",
    "AmfEventType",
    "AmfId",
    "AmfName",
    "AmfStatusChangeNotification",
    "AmfStatusInfo",
    "Area",
    "AreaCode",
    "AreaOfValidity",
    "Arp",
    "ArpPriorityLevel",
    "AssignEbiError",
    "AssignEbiFailed",
    "AssignedEbiData",
    "BitRate",
    "Bytes",
    "CipheringAlgorithm",
    "ConfiguredSnssai",
    "CoreNetworkType",
    "CorrelationId",
    "CreateUeContextResponse201",
    "DateTime",
    "Dnn",
    "DrxParameter",
    "EbiArpMapping",
    "Ecgi",
    "EpsBearerId",
    "EpsBearerId2",
    "EutraCellId",
    "EutraLocation",
    "ExpectedUeBehavior",
    "FiveGMmCapability",
    "FiveQi",
    "GNbId",
    "GlobalRanNodeId",
    "Gpsi",
    "GroupId",
    "Guami",
    "IntegrityAlgorithm",
    "InvalidParam",
    "Ipv4Addr",
    "Ipv6Addr",
    "KeyAmf",
    "KeyAmfType",
    "LadnInfo",
    "LocationFilter",
    "Mcc",
    "MmContext",
    "Mnc",
    "N1MessageClass",
    "N1MessageContainer",
    "N1MessageNotification",
    "N1N2MessageTransferCause",
    "N1N2MessageTransferError",
    "N1N2MessageTransferReqData",
    "N1N2MessageTransferRequestBody",
    "N1N2MessageTransferRspData",
    "N1N2MsgTxfrErrDetail",
    "N1N2MsgTxfrFailureNotification",
    "N2InfoContainer",
    "N2InfoContent",
    "N2InfoNotifyReason",
    "N2InformationClass",
    "N2InformationNotification",
    "N2InformationTransferError",
    "N2InformationTransferReqData",
    "N2InformationTransferResult",
    "N2InformationTransferRspData",
    "N2RanInformation",
    "N2SmInformation",
    "N3GaLocation",
    "N3IwfId",
    "NasCount",
    "NasSecurityMode",
    "Ncgi",
    "NfGroupId",
    "NfInstanceId",
    "NgApCause",
    "NgKsi",
    "NgRanTargetId",
    "NgapIeType",
    "NgeNbId",
    "NonUeN2InfoSubscriptionCreatedData",
    "NonUeN2MessageTransferRequestBody",
    "NrCellId",
    "NrLocation",
    "NrppaInformation",
    "NsiId",
    "NsiInformation",
    "NssaiMapping",
    "OauthScope",
    "OmcIdentifier",
    "PduSessionContext",
    "PduSessionId",
    "Pei",
    "PlmnId",
    "Ppi",
    "PreemptionCapability",
    "PreemptionVulnerability",
    "PresenceInfo",
    "PresenceState",
    "ProblemDetails",
    "PwsErrorData",
    "PwsInformation",
    "PwsResponseData",
    "RatSelector",
    "RatType",
    "RefToBinaryData",
    "RegistrationContextContainer",
    "RestrictionType",
    "RfspIndex",
    "S1UeNetworkCapability",
    "ScType",
    "SeafData",
    "ServiceAreaRestriction",
    "SmsSupport",
    "Snssai",
    "StatusChange",
    "SubscribedDataFilter",
    "SubscriptionData",
    "Supi",
    "SupportedFeatures",
    "Tac",
    "Tai",
    "TimeZone",
    "TraceData",
    "TraceDepth",
    "TransferReason",
    "UeContext",
    "UeContextCreateData",
    "UeContextCreateError",
    "UeContextCreatedData",
    "UeContextTransferReqData",
    "UeContextTransferRequestBody",
    "UeContextTransferResponse200",
    "UeContextTransferRspData",
    "UeContextTransferStatus",
    "UeN1N2InfoSubscriptionCreatedData",
    "UeRegStatusUpdateRspData",
    "UeSecurityCapability",
    "Uint16",
    "Uinteger",
    "Uri",
    "UserLocation",
]
