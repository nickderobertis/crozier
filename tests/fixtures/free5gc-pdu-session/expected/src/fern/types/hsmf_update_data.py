

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .cause import Cause
from .eps_bearer_id import EpsBearerId
from .eps_interworking_indication import EpsInterworkingIndication
from .ng_ap_cause import NgApCause
from .pdu_session_notify_item import PduSessionNotifyItem
from .plmn_id import PlmnId
from .qos_flow_item import QosFlowItem
from .qos_flow_notify_item import QosFlowNotifyItem
from .rat_type import RatType
from .ref_to_binary_data import RefToBinaryData
from .request_indication import RequestIndication
from .secondary_rat_usage_report import SecondaryRatUsageReport
from .tunnel_info import TunnelInfo
from .user_location import UserLocation


class HsmfUpdateData(UniversalBaseModel):
    request_indication: typing_extensions.Annotated[
        RequestIndication, FieldMetadata(alias="requestIndication"), pydantic.Field(alias="requestIndication")
    ]
    pei: typing.Optional[str] = None
    vcn_tunnel_info: typing_extensions.Annotated[
        typing.Optional[TunnelInfo], FieldMetadata(alias="vcnTunnelInfo"), pydantic.Field(alias="vcnTunnelInfo")
    ] = None
    serving_network: typing_extensions.Annotated[
        typing.Optional[PlmnId], FieldMetadata(alias="servingNetwork"), pydantic.Field(alias="servingNetwork")
    ] = None
    an_type: typing_extensions.Annotated[
        typing.Optional[AccessType], FieldMetadata(alias="anType"), pydantic.Field(alias="anType")
    ] = None
    rat_type: typing_extensions.Annotated[
        typing.Optional[RatType], FieldMetadata(alias="ratType"), pydantic.Field(alias="ratType")
    ] = None
    ue_location: typing_extensions.Annotated[
        typing.Optional[UserLocation], FieldMetadata(alias="ueLocation"), pydantic.Field(alias="ueLocation")
    ] = None
    ue_time_zone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ueTimeZone"), pydantic.Field(alias="ueTimeZone")
    ] = None
    add_ue_location: typing_extensions.Annotated[
        typing.Optional[UserLocation], FieldMetadata(alias="addUeLocation"), pydantic.Field(alias="addUeLocation")
    ] = None
    pause_charging: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="pauseCharging"), pydantic.Field(alias="pauseCharging")
    ] = None
    pti: typing.Optional[int] = None
    n1sm_info_from_ue: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmInfoFromUe"), pydantic.Field(alias="n1SmInfoFromUe")
    ] = None
    unknown_n1sm_info: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData],
        FieldMetadata(alias="unknownN1SmInfo"),
        pydantic.Field(alias="unknownN1SmInfo"),
    ] = None
    qos_flows_rel_notify_list: typing_extensions.Annotated[
        typing.Optional[typing.List[QosFlowItem]],
        FieldMetadata(alias="qosFlowsRelNotifyList"),
        pydantic.Field(alias="qosFlowsRelNotifyList"),
    ] = None
    qos_flows_notify_list: typing_extensions.Annotated[
        typing.Optional[typing.List[QosFlowNotifyItem]],
        FieldMetadata(alias="qosFlowsNotifyList"),
        pydantic.Field(alias="qosFlowsNotifyList"),
    ] = None
    notify_list: typing_extensions.Annotated[
        typing.Optional[typing.List[PduSessionNotifyItem]],
        FieldMetadata(alias="NotifyList"),
        pydantic.Field(alias="NotifyList"),
    ] = None
    eps_bearer_id: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="epsBearerId"),
        pydantic.Field(alias="epsBearerId"),
    ] = None
    ho_preparation_indication: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hoPreparationIndication"),
        pydantic.Field(alias="hoPreparationIndication"),
    ] = None
    revoke_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="revokeEbiList"),
        pydantic.Field(alias="revokeEbiList"),
    ] = None
    cause: typing.Optional[Cause] = None
    ng_ap_cause: typing_extensions.Annotated[
        typing.Optional[NgApCause], FieldMetadata(alias="ngApCause"), pydantic.Field(alias="ngApCause")
    ] = None
    f_5g_mm_cause_value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="5gMmCauseValue"), pydantic.Field(alias="5gMmCauseValue")
    ] = None
    always_on_requested: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="alwaysOnRequested"), pydantic.Field(alias="alwaysOnRequested")
    ] = None
    eps_interworking_ind: typing_extensions.Annotated[
        typing.Optional[EpsInterworkingIndication],
        FieldMetadata(alias="epsInterworkingInd"),
        pydantic.Field(alias="epsInterworkingInd"),
    ] = None
    secondary_rat_usage_report: typing_extensions.Annotated[
        typing.Optional[typing.List[SecondaryRatUsageReport]],
        FieldMetadata(alias="secondaryRatUsageReport"),
        pydantic.Field(alias="secondaryRatUsageReport"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
