

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ambr import Ambr
from .eps_bearer_info import EpsBearerInfo
from .eps_pdn_cnx_info import EpsPdnCnxInfo
from .ipv6prefix import Ipv6Prefix
from .max_integrity_protected_data_rate import MaxIntegrityProtectedDataRate
from .pdu_session_type import PduSessionType
from .qos_flow_setup_item import QosFlowSetupItem
from .ref_to_binary_data import RefToBinaryData
from .roaming_charging_profile import RoamingChargingProfile
from .snssai import Snssai
from .tunnel_info import TunnelInfo
from .up_security import UpSecurity


class PduSessionCreatedData(UniversalBaseModel):
    pdu_session_type: typing_extensions.Annotated[
        PduSessionType, FieldMetadata(alias="pduSessionType"), pydantic.Field(alias="pduSessionType")
    ]
    ssc_mode: typing_extensions.Annotated[str, FieldMetadata(alias="sscMode"), pydantic.Field(alias="sscMode")]
    hcn_tunnel_info: typing_extensions.Annotated[
        TunnelInfo, FieldMetadata(alias="hcnTunnelInfo"), pydantic.Field(alias="hcnTunnelInfo")
    ]
    session_ambr: typing_extensions.Annotated[
        Ambr, FieldMetadata(alias="sessionAmbr"), pydantic.Field(alias="sessionAmbr")
    ]
    qos_flows_setup_list: typing_extensions.Annotated[
        typing.List[QosFlowSetupItem],
        FieldMetadata(alias="qosFlowsSetupList"),
        pydantic.Field(alias="qosFlowsSetupList"),
    ]
    h_smf_instance_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="hSmfInstanceId"), pydantic.Field(alias="hSmfInstanceId")
    ]
    pdu_session_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pduSessionId"), pydantic.Field(alias="pduSessionId")
    ] = None
    s_nssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="sNssai"), pydantic.Field(alias="sNssai")
    ] = None
    enable_pause_charging: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="enablePauseCharging"), pydantic.Field(alias="enablePauseCharging")
    ] = None
    ue_ipv4address: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ueIpv4Address"), pydantic.Field(alias="ueIpv4Address")
    ] = None
    ue_ipv6prefix: typing_extensions.Annotated[
        typing.Optional[Ipv6Prefix], FieldMetadata(alias="ueIpv6Prefix"), pydantic.Field(alias="ueIpv6Prefix")
    ] = None
    n1sm_info_to_ue: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmInfoToUe"), pydantic.Field(alias="n1SmInfoToUe")
    ] = None
    eps_pdn_cnx_info: typing_extensions.Annotated[
        typing.Optional[EpsPdnCnxInfo], FieldMetadata(alias="epsPdnCnxInfo"), pydantic.Field(alias="epsPdnCnxInfo")
    ] = None
    eps_bearer_info: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerInfo]],
        FieldMetadata(alias="epsBearerInfo"),
        pydantic.Field(alias="epsBearerInfo"),
    ] = None
    supported_features: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supportedFeatures"), pydantic.Field(alias="supportedFeatures")
    ] = None
    max_integrity_protected_data_rate: typing_extensions.Annotated[
        typing.Optional[MaxIntegrityProtectedDataRate],
        FieldMetadata(alias="maxIntegrityProtectedDataRate"),
        pydantic.Field(alias="maxIntegrityProtectedDataRate"),
    ] = None
    always_on_granted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="alwaysOnGranted"), pydantic.Field(alias="alwaysOnGranted")
    ] = None
    up_security: typing_extensions.Annotated[
        typing.Optional[UpSecurity], FieldMetadata(alias="upSecurity"), pydantic.Field(alias="upSecurity")
    ] = None
    roaming_charging_profile: typing_extensions.Annotated[
        typing.Optional[RoamingChargingProfile],
        FieldMetadata(alias="roamingChargingProfile"),
        pydantic.Field(alias="roamingChargingProfile"),
    ] = None
    h_smf_service_instance_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="hSmfServiceInstanceId"),
        pydantic.Field(alias="hSmfServiceInstanceId"),
    ] = None
    recovery_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="recoveryTime"), pydantic.Field(alias="recoveryTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
