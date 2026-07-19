



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .access_type import AccessType
    from .additional_qos_flow_info import AdditionalQosFlowInfo
    from .ambr import Ambr
    from .amf_id import AmfId
    from .amf_name import AmfName
    from .arp import Arp
    from .arp_priority_level import ArpPriorityLevel
    from .aver_window import AverWindow
    from .backup_amf_info import BackupAmfInfo
    from .bit_rate import BitRate
    from .bytes import Bytes
    from .cause import Cause
    from .date_time import DateTime
    from .dnn import Dnn
    from .dnn_selection_mode import DnnSelectionMode
    from .duration_sec import DurationSec
    from .dynamic5qi import Dynamic5Qi
    from .ebi_arp_mapping import EbiArpMapping
    from .ecgi import Ecgi
    from .eps_bearer_container import EpsBearerContainer
    from .eps_bearer_id import EpsBearerId
    from .eps_bearer_info import EpsBearerInfo
    from .eps_interworking_indication import EpsInterworkingIndication
    from .eps_pdn_cnx_container import EpsPdnCnxContainer
    from .eps_pdn_cnx_info import EpsPdnCnxInfo
    from .eutra_cell_id import EutraCellId
    from .eutra_location import EutraLocation
    from .five_g_mm_cause import FiveGMmCause
    from .five_qi import FiveQi
    from .five_qi_priority_level import FiveQiPriorityLevel
    from .g_nb_id import GNbId
    from .gbr_qos_flow_information import GbrQosFlowInformation
    from .global_ran_node_id import GlobalRanNodeId
    from .gpsi import Gpsi
    from .guami import Guami
    from .ho_state import HoState
    from .hsmf_update_data import HsmfUpdateData
    from .hsmf_update_error import HsmfUpdateError
    from .hsmf_updated_data import HsmfUpdatedData
    from .int64 import Int64
    from .invalid_param import InvalidParam
    from .ipv4addr import Ipv4Addr
    from .ipv6addr import Ipv6Addr
    from .ipv6prefix import Ipv6Prefix
    from .max_data_burst_vol import MaxDataBurstVol
    from .max_integrity_protected_data_rate import MaxIntegrityProtectedDataRate
    from .mcc import Mcc
    from .mme_capabilities import MmeCapabilities
    from .mnc import Mnc
    from .n2sm_info_type import N2SmInfoType
    from .n3ga_location import N3GaLocation
    from .n3iwf_id import N3IwfId
    from .ncgi import Ncgi
    from .nf_group_id import NfGroupId
    from .nf_instance_id import NfInstanceId
    from .ng_ap_cause import NgApCause
    from .nge_nb_id import NgeNbId
    from .non_dynamic5qi import NonDynamic5Qi
    from .notification_cause import NotificationCause
    from .notification_control import NotificationControl
    from .nr_cell_id import NrCellId
    from .nr_location import NrLocation
    from .oauth_scope import OauthScope
    from .packet_del_budget import PacketDelBudget
    from .packet_err_rate import PacketErrRate
    from .packet_loss_rate import PacketLossRate
    from .partial_record_method import PartialRecordMethod
    from .pdu_session_create_data import PduSessionCreateData
    from .pdu_session_create_error import PduSessionCreateError
    from .pdu_session_created_data import PduSessionCreatedData
    from .pdu_session_id import PduSessionId
    from .pdu_session_notify_item import PduSessionNotifyItem
    from .pdu_session_type import PduSessionType
    from .pei import Pei
    from .plmn_id import PlmnId
    from .post_pdu_sessions_request_body import PostPduSessionsRequestBody
    from .post_pdu_sessions_response201 import PostPduSessionsResponse201
    from .post_pdu_sessions_response400 import PostPduSessionsResponse400
    from .post_sm_contexts_response201 import PostSmContextsResponse201
    from .post_sm_contexts_response400 import PostSmContextsResponse400
    from .post_sm_contexts_response403 import PostSmContextsResponse403
    from .post_sm_contexts_response404 import PostSmContextsResponse404
    from .post_sm_contexts_response500 import PostSmContextsResponse500
    from .post_sm_contexts_response503 import PostSmContextsResponse503
    from .post_sm_contexts_response504 import PostSmContextsResponse504
    from .preemption_capability import PreemptionCapability
    from .preemption_vulnerability import PreemptionVulnerability
    from .presence_state import PresenceState
    from .problem_details import ProblemDetails
    from .procedure_transaction_id import ProcedureTransactionId
    from .qfi import Qfi
    from .qos_flow_add_modify_request_item import QosFlowAddModifyRequestItem
    from .qos_flow_item import QosFlowItem
    from .qos_flow_notify_item import QosFlowNotifyItem
    from .qos_flow_profile import QosFlowProfile
    from .qos_flow_release_request_item import QosFlowReleaseRequestItem
    from .qos_flow_setup_item import QosFlowSetupItem
    from .qos_flow_usage_report import QosFlowUsageReport
    from .qos_resource_type import QosResourceType
    from .rat_type import RatType
    from .ref_to_binary_data import RefToBinaryData
    from .reflective_qo_s_attribute import ReflectiveQoSAttribute
    from .release_sm_context_request_body import ReleaseSmContextRequestBody
    from .released_data import ReleasedData
    from .request_indication import RequestIndication
    from .request_type import RequestType
    from .resource_status import ResourceStatus
    from .roaming_charging_profile import RoamingChargingProfile
    from .secondary_rat_usage_report import SecondaryRatUsageReport
    from .service_name import ServiceName
    from .sm_context_create_data import SmContextCreateData
    from .sm_context_create_error import SmContextCreateError
    from .sm_context_created_data import SmContextCreatedData
    from .sm_context_release_data import SmContextReleaseData
    from .sm_context_retrieved_data import SmContextRetrievedData
    from .sm_context_status_notification import SmContextStatusNotification
    from .sm_context_update_data import SmContextUpdateData
    from .sm_context_update_error import SmContextUpdateError
    from .sm_context_updated_data import SmContextUpdatedData
    from .snssai import Snssai
    from .status_info import StatusInfo
    from .status_notification import StatusNotification
    from .supi import Supi
    from .supported_features import SupportedFeatures
    from .tac import Tac
    from .tai import Tai
    from .teid import Teid
    from .time_zone import TimeZone
    from .trace_data import TraceData
    from .trace_depth import TraceDepth
    from .trigger import Trigger
    from .trigger_category import TriggerCategory
    from .trigger_type import TriggerType
    from .tunnel_info import TunnelInfo
    from .uint32 import Uint32
    from .uinteger import Uinteger
    from .up_cnx_state import UpCnxState
    from .up_confidentiality import UpConfidentiality
    from .up_integrity import UpIntegrity
    from .up_security import UpSecurity
    from .update_pdu_session_request_body import UpdatePduSessionRequestBody
    from .update_pdu_session_response200 import UpdatePduSessionResponse200
    from .update_pdu_session_response400 import UpdatePduSessionResponse400
    from .update_sm_context_request_body import UpdateSmContextRequestBody
    from .update_sm_context_response200 import UpdateSmContextResponse200
    from .update_sm_context_response400 import UpdateSmContextResponse400
    from .update_sm_context_response403 import UpdateSmContextResponse403
    from .update_sm_context_response404 import UpdateSmContextResponse404
    from .update_sm_context_response500 import UpdateSmContextResponse500
    from .update_sm_context_response503 import UpdateSmContextResponse503
    from .uri import Uri
    from .user_location import UserLocation
    from .vsmf_update_data import VsmfUpdateData
    from .vsmf_update_error import VsmfUpdateError
    from .vsmf_updated_data import VsmfUpdatedData
_dynamic_imports: typing.Dict[str, str] = {
    "AccessType": ".access_type",
    "AdditionalQosFlowInfo": ".additional_qos_flow_info",
    "Ambr": ".ambr",
    "AmfId": ".amf_id",
    "AmfName": ".amf_name",
    "Arp": ".arp",
    "ArpPriorityLevel": ".arp_priority_level",
    "AverWindow": ".aver_window",
    "BackupAmfInfo": ".backup_amf_info",
    "BitRate": ".bit_rate",
    "Bytes": ".bytes",
    "Cause": ".cause",
    "DateTime": ".date_time",
    "Dnn": ".dnn",
    "DnnSelectionMode": ".dnn_selection_mode",
    "DurationSec": ".duration_sec",
    "Dynamic5Qi": ".dynamic5qi",
    "EbiArpMapping": ".ebi_arp_mapping",
    "Ecgi": ".ecgi",
    "EpsBearerContainer": ".eps_bearer_container",
    "EpsBearerId": ".eps_bearer_id",
    "EpsBearerInfo": ".eps_bearer_info",
    "EpsInterworkingIndication": ".eps_interworking_indication",
    "EpsPdnCnxContainer": ".eps_pdn_cnx_container",
    "EpsPdnCnxInfo": ".eps_pdn_cnx_info",
    "EutraCellId": ".eutra_cell_id",
    "EutraLocation": ".eutra_location",
    "FiveGMmCause": ".five_g_mm_cause",
    "FiveQi": ".five_qi",
    "FiveQiPriorityLevel": ".five_qi_priority_level",
    "GNbId": ".g_nb_id",
    "GbrQosFlowInformation": ".gbr_qos_flow_information",
    "GlobalRanNodeId": ".global_ran_node_id",
    "Gpsi": ".gpsi",
    "Guami": ".guami",
    "HoState": ".ho_state",
    "HsmfUpdateData": ".hsmf_update_data",
    "HsmfUpdateError": ".hsmf_update_error",
    "HsmfUpdatedData": ".hsmf_updated_data",
    "Int64": ".int64",
    "InvalidParam": ".invalid_param",
    "Ipv4Addr": ".ipv4addr",
    "Ipv6Addr": ".ipv6addr",
    "Ipv6Prefix": ".ipv6prefix",
    "MaxDataBurstVol": ".max_data_burst_vol",
    "MaxIntegrityProtectedDataRate": ".max_integrity_protected_data_rate",
    "Mcc": ".mcc",
    "MmeCapabilities": ".mme_capabilities",
    "Mnc": ".mnc",
    "N2SmInfoType": ".n2sm_info_type",
    "N3GaLocation": ".n3ga_location",
    "N3IwfId": ".n3iwf_id",
    "Ncgi": ".ncgi",
    "NfGroupId": ".nf_group_id",
    "NfInstanceId": ".nf_instance_id",
    "NgApCause": ".ng_ap_cause",
    "NgeNbId": ".nge_nb_id",
    "NonDynamic5Qi": ".non_dynamic5qi",
    "NotificationCause": ".notification_cause",
    "NotificationControl": ".notification_control",
    "NrCellId": ".nr_cell_id",
    "NrLocation": ".nr_location",
    "OauthScope": ".oauth_scope",
    "PacketDelBudget": ".packet_del_budget",
    "PacketErrRate": ".packet_err_rate",
    "PacketLossRate": ".packet_loss_rate",
    "PartialRecordMethod": ".partial_record_method",
    "PduSessionCreateData": ".pdu_session_create_data",
    "PduSessionCreateError": ".pdu_session_create_error",
    "PduSessionCreatedData": ".pdu_session_created_data",
    "PduSessionId": ".pdu_session_id",
    "PduSessionNotifyItem": ".pdu_session_notify_item",
    "PduSessionType": ".pdu_session_type",
    "Pei": ".pei",
    "PlmnId": ".plmn_id",
    "PostPduSessionsRequestBody": ".post_pdu_sessions_request_body",
    "PostPduSessionsResponse201": ".post_pdu_sessions_response201",
    "PostPduSessionsResponse400": ".post_pdu_sessions_response400",
    "PostSmContextsResponse201": ".post_sm_contexts_response201",
    "PostSmContextsResponse400": ".post_sm_contexts_response400",
    "PostSmContextsResponse403": ".post_sm_contexts_response403",
    "PostSmContextsResponse404": ".post_sm_contexts_response404",
    "PostSmContextsResponse500": ".post_sm_contexts_response500",
    "PostSmContextsResponse503": ".post_sm_contexts_response503",
    "PostSmContextsResponse504": ".post_sm_contexts_response504",
    "PreemptionCapability": ".preemption_capability",
    "PreemptionVulnerability": ".preemption_vulnerability",
    "PresenceState": ".presence_state",
    "ProblemDetails": ".problem_details",
    "ProcedureTransactionId": ".procedure_transaction_id",
    "Qfi": ".qfi",
    "QosFlowAddModifyRequestItem": ".qos_flow_add_modify_request_item",
    "QosFlowItem": ".qos_flow_item",
    "QosFlowNotifyItem": ".qos_flow_notify_item",
    "QosFlowProfile": ".qos_flow_profile",
    "QosFlowReleaseRequestItem": ".qos_flow_release_request_item",
    "QosFlowSetupItem": ".qos_flow_setup_item",
    "QosFlowUsageReport": ".qos_flow_usage_report",
    "QosResourceType": ".qos_resource_type",
    "RatType": ".rat_type",
    "RefToBinaryData": ".ref_to_binary_data",
    "ReflectiveQoSAttribute": ".reflective_qo_s_attribute",
    "ReleaseSmContextRequestBody": ".release_sm_context_request_body",
    "ReleasedData": ".released_data",
    "RequestIndication": ".request_indication",
    "RequestType": ".request_type",
    "ResourceStatus": ".resource_status",
    "RoamingChargingProfile": ".roaming_charging_profile",
    "SecondaryRatUsageReport": ".secondary_rat_usage_report",
    "ServiceName": ".service_name",
    "SmContextCreateData": ".sm_context_create_data",
    "SmContextCreateError": ".sm_context_create_error",
    "SmContextCreatedData": ".sm_context_created_data",
    "SmContextReleaseData": ".sm_context_release_data",
    "SmContextRetrievedData": ".sm_context_retrieved_data",
    "SmContextStatusNotification": ".sm_context_status_notification",
    "SmContextUpdateData": ".sm_context_update_data",
    "SmContextUpdateError": ".sm_context_update_error",
    "SmContextUpdatedData": ".sm_context_updated_data",
    "Snssai": ".snssai",
    "StatusInfo": ".status_info",
    "StatusNotification": ".status_notification",
    "Supi": ".supi",
    "SupportedFeatures": ".supported_features",
    "Tac": ".tac",
    "Tai": ".tai",
    "Teid": ".teid",
    "TimeZone": ".time_zone",
    "TraceData": ".trace_data",
    "TraceDepth": ".trace_depth",
    "Trigger": ".trigger",
    "TriggerCategory": ".trigger_category",
    "TriggerType": ".trigger_type",
    "TunnelInfo": ".tunnel_info",
    "Uint32": ".uint32",
    "Uinteger": ".uinteger",
    "UpCnxState": ".up_cnx_state",
    "UpConfidentiality": ".up_confidentiality",
    "UpIntegrity": ".up_integrity",
    "UpSecurity": ".up_security",
    "UpdatePduSessionRequestBody": ".update_pdu_session_request_body",
    "UpdatePduSessionResponse200": ".update_pdu_session_response200",
    "UpdatePduSessionResponse400": ".update_pdu_session_response400",
    "UpdateSmContextRequestBody": ".update_sm_context_request_body",
    "UpdateSmContextResponse200": ".update_sm_context_response200",
    "UpdateSmContextResponse400": ".update_sm_context_response400",
    "UpdateSmContextResponse403": ".update_sm_context_response403",
    "UpdateSmContextResponse404": ".update_sm_context_response404",
    "UpdateSmContextResponse500": ".update_sm_context_response500",
    "UpdateSmContextResponse503": ".update_sm_context_response503",
    "Uri": ".uri",
    "UserLocation": ".user_location",
    "VsmfUpdateData": ".vsmf_update_data",
    "VsmfUpdateError": ".vsmf_update_error",
    "VsmfUpdatedData": ".vsmf_updated_data",
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
    "AdditionalQosFlowInfo",
    "Ambr",
    "AmfId",
    "AmfName",
    "Arp",
    "ArpPriorityLevel",
    "AverWindow",
    "BackupAmfInfo",
    "BitRate",
    "Bytes",
    "Cause",
    "DateTime",
    "Dnn",
    "DnnSelectionMode",
    "DurationSec",
    "Dynamic5Qi",
    "EbiArpMapping",
    "Ecgi",
    "EpsBearerContainer",
    "EpsBearerId",
    "EpsBearerInfo",
    "EpsInterworkingIndication",
    "EpsPdnCnxContainer",
    "EpsPdnCnxInfo",
    "EutraCellId",
    "EutraLocation",
    "FiveGMmCause",
    "FiveQi",
    "FiveQiPriorityLevel",
    "GNbId",
    "GbrQosFlowInformation",
    "GlobalRanNodeId",
    "Gpsi",
    "Guami",
    "HoState",
    "HsmfUpdateData",
    "HsmfUpdateError",
    "HsmfUpdatedData",
    "Int64",
    "InvalidParam",
    "Ipv4Addr",
    "Ipv6Addr",
    "Ipv6Prefix",
    "MaxDataBurstVol",
    "MaxIntegrityProtectedDataRate",
    "Mcc",
    "MmeCapabilities",
    "Mnc",
    "N2SmInfoType",
    "N3GaLocation",
    "N3IwfId",
    "Ncgi",
    "NfGroupId",
    "NfInstanceId",
    "NgApCause",
    "NgeNbId",
    "NonDynamic5Qi",
    "NotificationCause",
    "NotificationControl",
    "NrCellId",
    "NrLocation",
    "OauthScope",
    "PacketDelBudget",
    "PacketErrRate",
    "PacketLossRate",
    "PartialRecordMethod",
    "PduSessionCreateData",
    "PduSessionCreateError",
    "PduSessionCreatedData",
    "PduSessionId",
    "PduSessionNotifyItem",
    "PduSessionType",
    "Pei",
    "PlmnId",
    "PostPduSessionsRequestBody",
    "PostPduSessionsResponse201",
    "PostPduSessionsResponse400",
    "PostSmContextsResponse201",
    "PostSmContextsResponse400",
    "PostSmContextsResponse403",
    "PostSmContextsResponse404",
    "PostSmContextsResponse500",
    "PostSmContextsResponse503",
    "PostSmContextsResponse504",
    "PreemptionCapability",
    "PreemptionVulnerability",
    "PresenceState",
    "ProblemDetails",
    "ProcedureTransactionId",
    "Qfi",
    "QosFlowAddModifyRequestItem",
    "QosFlowItem",
    "QosFlowNotifyItem",
    "QosFlowProfile",
    "QosFlowReleaseRequestItem",
    "QosFlowSetupItem",
    "QosFlowUsageReport",
    "QosResourceType",
    "RatType",
    "RefToBinaryData",
    "ReflectiveQoSAttribute",
    "ReleaseSmContextRequestBody",
    "ReleasedData",
    "RequestIndication",
    "RequestType",
    "ResourceStatus",
    "RoamingChargingProfile",
    "SecondaryRatUsageReport",
    "ServiceName",
    "SmContextCreateData",
    "SmContextCreateError",
    "SmContextCreatedData",
    "SmContextReleaseData",
    "SmContextRetrievedData",
    "SmContextStatusNotification",
    "SmContextUpdateData",
    "SmContextUpdateError",
    "SmContextUpdatedData",
    "Snssai",
    "StatusInfo",
    "StatusNotification",
    "Supi",
    "SupportedFeatures",
    "Tac",
    "Tai",
    "Teid",
    "TimeZone",
    "TraceData",
    "TraceDepth",
    "Trigger",
    "TriggerCategory",
    "TriggerType",
    "TunnelInfo",
    "Uint32",
    "Uinteger",
    "UpCnxState",
    "UpConfidentiality",
    "UpIntegrity",
    "UpSecurity",
    "UpdatePduSessionRequestBody",
    "UpdatePduSessionResponse200",
    "UpdatePduSessionResponse400",
    "UpdateSmContextRequestBody",
    "UpdateSmContextResponse200",
    "UpdateSmContextResponse400",
    "UpdateSmContextResponse403",
    "UpdateSmContextResponse404",
    "UpdateSmContextResponse500",
    "UpdateSmContextResponse503",
    "Uri",
    "UserLocation",
    "VsmfUpdateData",
    "VsmfUpdateError",
    "VsmfUpdatedData",
]
