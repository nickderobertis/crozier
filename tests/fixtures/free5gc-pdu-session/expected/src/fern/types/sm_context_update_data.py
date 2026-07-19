

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .backup_amf_info import BackupAmfInfo
from .cause import Cause
from .eps_bearer_container import EpsBearerContainer
from .eps_bearer_id import EpsBearerId
from .eps_interworking_indication import EpsInterworkingIndication
from .guami import Guami
from .ho_state import HoState
from .n2sm_info_type import N2SmInfoType
from .ng_ap_cause import NgApCause
from .plmn_id import PlmnId
from .presence_state import PresenceState
from .rat_type import RatType
from .ref_to_binary_data import RefToBinaryData
from .snssai import Snssai
from .trace_data import TraceData
from .up_cnx_state import UpCnxState
from .user_location import UserLocation


class SmContextUpdateData(UniversalBaseModel):
    pei: typing.Optional[str] = None
    gpsi: typing.Optional[str] = None
    serving_nf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="servingNfId"), pydantic.Field(alias="servingNfId")
    ] = None
    guami: typing.Optional[Guami] = None
    serving_network: typing_extensions.Annotated[
        typing.Optional[PlmnId], FieldMetadata(alias="servingNetwork"), pydantic.Field(alias="servingNetwork")
    ] = None
    backup_amf_info: typing_extensions.Annotated[
        typing.Optional[typing.List[BackupAmfInfo]],
        FieldMetadata(alias="backupAmfInfo"),
        pydantic.Field(alias="backupAmfInfo"),
    ] = None
    an_type: typing_extensions.Annotated[
        typing.Optional[AccessType], FieldMetadata(alias="anType"), pydantic.Field(alias="anType")
    ] = None
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
    up_cnx_state: typing_extensions.Annotated[
        typing.Optional[UpCnxState], FieldMetadata(alias="upCnxState"), pydantic.Field(alias="upCnxState")
    ] = None
    ho_state: typing_extensions.Annotated[
        typing.Optional[HoState], FieldMetadata(alias="hoState"), pydantic.Field(alias="hoState")
    ] = None
    to_be_switched: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="toBeSwitched"), pydantic.Field(alias="toBeSwitched")
    ] = None
    failed_to_be_switched: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="failedToBeSwitched"), pydantic.Field(alias="failedToBeSwitched")
    ] = None
    n1sm_msg: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmMsg"), pydantic.Field(alias="n1SmMsg")
    ] = None
    n2sm_info: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n2SmInfo"), pydantic.Field(alias="n2SmInfo")
    ] = None
    n2sm_info_type: typing_extensions.Annotated[
        typing.Optional[N2SmInfoType], FieldMetadata(alias="n2SmInfoType"), pydantic.Field(alias="n2SmInfoType")
    ] = None
    target_serving_nf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetServingNfId"), pydantic.Field(alias="targetServingNfId")
    ] = None
    sm_context_status_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="smContextStatusUri"), pydantic.Field(alias="smContextStatusUri")
    ] = None
    data_forwarding: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="dataForwarding"), pydantic.Field(alias="dataForwarding")
    ] = None
    eps_bearer_setup: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerContainer]],
        FieldMetadata(alias="epsBearerSetup"),
        pydantic.Field(alias="epsBearerSetup"),
    ] = None
    revoke_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="revokeEbiList"),
        pydantic.Field(alias="revokeEbiList"),
    ] = None
    release: typing.Optional[bool] = None
    cause: typing.Optional[Cause] = None
    ng_ap_cause: typing_extensions.Annotated[
        typing.Optional[NgApCause], FieldMetadata(alias="ngApCause"), pydantic.Field(alias="ngApCause")
    ] = None
    f_5g_mm_cause_value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="5gMmCauseValue"), pydantic.Field(alias="5gMmCauseValue")
    ] = None
    s_nssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="sNssai"), pydantic.Field(alias="sNssai")
    ] = None
    trace_data: typing_extensions.Annotated[
        typing.Optional[TraceData], FieldMetadata(alias="traceData"), pydantic.Field(alias="traceData")
    ] = None
    eps_interworking_ind: typing_extensions.Annotated[
        typing.Optional[EpsInterworkingIndication],
        FieldMetadata(alias="epsInterworkingInd"),
        pydantic.Field(alias="epsInterworkingInd"),
    ] = None
    an_type_can_be_changed: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="anTypeCanBeChanged"), pydantic.Field(alias="anTypeCanBeChanged")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
