

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .dnn_selection_mode import DnnSelectionMode
from .eps_bearer_id import EpsBearerId
from .eps_interworking_indication import EpsInterworkingIndication
from .plmn_id import PlmnId
from .rat_type import RatType
from .ref_to_binary_data import RefToBinaryData
from .request_type import RequestType
from .roaming_charging_profile import RoamingChargingProfile
from .snssai import Snssai
from .tunnel_info import TunnelInfo
from .user_location import UserLocation


class PduSessionCreateData(UniversalBaseModel):
    supi: typing.Optional[str] = None
    unauthenticated_supi: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="unauthenticatedSupi"), pydantic.Field(alias="unauthenticatedSupi")
    ] = None
    pei: typing.Optional[str] = None
    pdu_session_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pduSessionId"), pydantic.Field(alias="pduSessionId")
    ] = None
    dnn: str
    s_nssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="sNssai"), pydantic.Field(alias="sNssai")
    ] = None
    vsmf_id: typing_extensions.Annotated[str, FieldMetadata(alias="vsmfId"), pydantic.Field(alias="vsmfId")]
    serving_network: typing_extensions.Annotated[
        PlmnId, FieldMetadata(alias="servingNetwork"), pydantic.Field(alias="servingNetwork")
    ]
    request_type: typing_extensions.Annotated[
        typing.Optional[RequestType], FieldMetadata(alias="requestType"), pydantic.Field(alias="requestType")
    ] = None
    eps_bearer_id: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="epsBearerId"),
        pydantic.Field(alias="epsBearerId"),
    ] = None
    pgw_s8c_fteid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pgwS8cFteid"), pydantic.Field(alias="pgwS8cFteid")
    ] = None
    vsmf_pdu_session_uri: typing_extensions.Annotated[
        str, FieldMetadata(alias="vsmfPduSessionUri"), pydantic.Field(alias="vsmfPduSessionUri")
    ]
    vcn_tunnel_info: typing_extensions.Annotated[
        TunnelInfo, FieldMetadata(alias="vcnTunnelInfo"), pydantic.Field(alias="vcnTunnelInfo")
    ]
    an_type: typing_extensions.Annotated[AccessType, FieldMetadata(alias="anType"), pydantic.Field(alias="anType")]
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
    gpsi: typing.Optional[str] = None
    n1sm_info_from_ue: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmInfoFromUe"), pydantic.Field(alias="n1SmInfoFromUe")
    ] = None
    unknown_n1sm_info: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData],
        FieldMetadata(alias="unknownN1SmInfo"),
        pydantic.Field(alias="unknownN1SmInfo"),
    ] = None
    supported_features: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supportedFeatures"), pydantic.Field(alias="supportedFeatures")
    ] = None
    h_pcf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hPcfId"), pydantic.Field(alias="hPcfId")
    ] = None
    ho_preparation_indication: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="hoPreparationIndication"),
        pydantic.Field(alias="hoPreparationIndication"),
    ] = None
    sel_mode: typing_extensions.Annotated[
        typing.Optional[DnnSelectionMode], FieldMetadata(alias="selMode"), pydantic.Field(alias="selMode")
    ] = None
    always_on_requested: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="alwaysOnRequested"), pydantic.Field(alias="alwaysOnRequested")
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
    v_smf_service_instance_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="vSmfServiceInstanceId"),
        pydantic.Field(alias="vSmfServiceInstanceId"),
    ] = None
    recovery_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="recoveryTime"), pydantic.Field(alias="recoveryTime")
    ] = None
    roaming_charging_profile: typing_extensions.Annotated[
        typing.Optional[RoamingChargingProfile],
        FieldMetadata(alias="roamingChargingProfile"),
        pydantic.Field(alias="roamingChargingProfile"),
    ] = None
    charging_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="chargingId"), pydantic.Field(alias="chargingId")
    ] = None
    old_pdu_session_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="oldPduSessionId"), pydantic.Field(alias="oldPduSessionId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
