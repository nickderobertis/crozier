

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .backup_amf_info import BackupAmfInfo
from .dnn_selection_mode import DnnSelectionMode
from .eps_interworking_indication import EpsInterworkingIndication
from .guami import Guami
from .ho_state import HoState
from .pdu_session_id import PduSessionId
from .plmn_id import PlmnId
from .presence_state import PresenceState
from .rat_type import RatType
from .ref_to_binary_data import RefToBinaryData
from .request_type import RequestType
from .service_name import ServiceName
from .snssai import Snssai
from .trace_data import TraceData
from .uri import Uri
from .user_location import UserLocation


class SmContextCreateData(UniversalBaseModel):
    supi: typing.Optional[str] = None
    unauthenticated_supi: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="unauthenticatedSupi"), pydantic.Field(alias="unauthenticatedSupi")
    ] = None
    pei: typing.Optional[str] = None
    gpsi: typing.Optional[str] = None
    pdu_session_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pduSessionId"), pydantic.Field(alias="pduSessionId")
    ] = None
    dnn: typing.Optional[str] = None
    s_nssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="sNssai"), pydantic.Field(alias="sNssai")
    ] = None
    hplmn_snssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="hplmnSnssai"), pydantic.Field(alias="hplmnSnssai")
    ] = None
    serving_nf_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="servingNfId"), pydantic.Field(alias="servingNfId")
    ]
    guami: typing.Optional[Guami] = None
    service_name: typing_extensions.Annotated[
        typing.Optional[ServiceName], FieldMetadata(alias="serviceName"), pydantic.Field(alias="serviceName")
    ] = None
    serving_network: typing_extensions.Annotated[
        PlmnId, FieldMetadata(alias="servingNetwork"), pydantic.Field(alias="servingNetwork")
    ]
    request_type: typing_extensions.Annotated[
        typing.Optional[RequestType], FieldMetadata(alias="requestType"), pydantic.Field(alias="requestType")
    ] = None
    n1sm_msg: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmMsg"), pydantic.Field(alias="n1SmMsg")
    ] = None
    an_type: typing_extensions.Annotated[AccessType, FieldMetadata(alias="anType"), pydantic.Field(alias="anType")]
    rat_type: typing_extensions.Annotated[
        typing.Optional[RatType], FieldMetadata(alias="ratType"), pydantic.Field(alias="ratType")
    ] = None
    presence_in_ladn: typing_extensions.Annotated[
        typing.Optional[PresenceState], FieldMetadata(alias="presenceInLadn"), pydantic.Field(alias="presenceInLadn")
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
    sm_context_status_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="smContextStatusUri"), pydantic.Field(alias="smContextStatusUri")
    ]
    h_smf_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hSmfUri"), pydantic.Field(alias="hSmfUri")
    ] = None
    additional_hsmf_uri: typing_extensions.Annotated[
        typing.Optional[typing.List[Uri]],
        FieldMetadata(alias="additionalHsmfUri"),
        pydantic.Field(alias="additionalHsmfUri"),
    ] = None
    old_pdu_session_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="oldPduSessionId"), pydantic.Field(alias="oldPduSessionId")
    ] = None
    pdu_sessions_activate_list: typing_extensions.Annotated[
        typing.Optional[typing.List[PduSessionId]],
        FieldMetadata(alias="pduSessionsActivateList"),
        pydantic.Field(alias="pduSessionsActivateList"),
    ] = None
    ue_eps_pdn_connection: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ueEpsPdnConnection"), pydantic.Field(alias="ueEpsPdnConnection")
    ] = None
    ho_state: typing_extensions.Annotated[
        typing.Optional[HoState], FieldMetadata(alias="hoState"), pydantic.Field(alias="hoState")
    ] = None
    pcf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pcfId"), pydantic.Field(alias="pcfId")
    ] = None
    nrf_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nrfUri"), pydantic.Field(alias="nrfUri")
    ] = None
    supported_features: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supportedFeatures"), pydantic.Field(alias="supportedFeatures")
    ] = None
    sel_mode: typing_extensions.Annotated[
        typing.Optional[DnnSelectionMode], FieldMetadata(alias="selMode"), pydantic.Field(alias="selMode")
    ] = None
    backup_amf_info: typing_extensions.Annotated[
        typing.Optional[typing.List[BackupAmfInfo]],
        FieldMetadata(alias="backupAmfInfo"),
        pydantic.Field(alias="backupAmfInfo"),
    ] = None
    trace_data: typing_extensions.Annotated[
        typing.Optional[TraceData], FieldMetadata(alias="traceData"), pydantic.Field(alias="traceData")
    ] = None
    udm_group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="udmGroupId"), pydantic.Field(alias="udmGroupId")
    ] = None
    routing_indicator: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="routingIndicator"), pydantic.Field(alias="routingIndicator")
    ] = None
    eps_interworking_ind: typing_extensions.Annotated[
        typing.Optional[EpsInterworkingIndication],
        FieldMetadata(alias="epsInterworkingInd"),
        pydantic.Field(alias="epsInterworkingInd"),
    ] = None
    indirect_forwarding_flag: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="indirectForwardingFlag"),
        pydantic.Field(alias="indirectForwardingFlag"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
