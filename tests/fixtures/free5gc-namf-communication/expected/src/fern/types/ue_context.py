

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .am_policy_req_trigger import AmPolicyReqTrigger
from .ambr import Ambr
from .amf_event_subscription import AmfEventSubscription
from .area import Area
from .core_network_type import CoreNetworkType
from .gpsi import Gpsi
from .group_id import GroupId
from .mm_context import MmContext
from .pdu_session_context import PduSessionContext
from .rat_type import RatType
from .seaf_data import SeafData
from .service_area_restriction import ServiceAreaRestriction
from .sms_support import SmsSupport
from .trace_data import TraceData


class UeContext(UniversalBaseModel):
    supi: typing.Optional[str] = None
    supi_unauth_ind: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="supiUnauthInd"), pydantic.Field(alias="supiUnauthInd")
    ] = None
    gpsi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Gpsi]], FieldMetadata(alias="gpsiList"), pydantic.Field(alias="gpsiList")
    ] = None
    pei: typing.Optional[str] = None
    udm_group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="udmGroupId"), pydantic.Field(alias="udmGroupId")
    ] = None
    ausf_group_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ausfGroupId"), pydantic.Field(alias="ausfGroupId")
    ] = None
    routing_indicator: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="routingIndicator"), pydantic.Field(alias="routingIndicator")
    ] = None
    group_list: typing_extensions.Annotated[
        typing.Optional[typing.List[GroupId]], FieldMetadata(alias="groupList"), pydantic.Field(alias="groupList")
    ] = None
    drx_parameter: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="drxParameter"), pydantic.Field(alias="drxParameter")
    ] = None
    sub_rfsp: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="subRfsp"), pydantic.Field(alias="subRfsp")
    ] = None
    used_rfsp: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="usedRfsp"), pydantic.Field(alias="usedRfsp")
    ] = None
    sub_ue_ambr: typing_extensions.Annotated[
        typing.Optional[Ambr], FieldMetadata(alias="subUeAmbr"), pydantic.Field(alias="subUeAmbr")
    ] = None
    sms_support: typing_extensions.Annotated[
        typing.Optional[SmsSupport], FieldMetadata(alias="smsSupport"), pydantic.Field(alias="smsSupport")
    ] = None
    smsf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="smsfId"), pydantic.Field(alias="smsfId")
    ] = None
    seaf_data: typing_extensions.Annotated[
        typing.Optional[SeafData], FieldMetadata(alias="seafData"), pydantic.Field(alias="seafData")
    ] = None
    f_5g_mm_capability: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="5gMmCapability"), pydantic.Field(alias="5gMmCapability")
    ] = None
    pcf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pcfId"), pydantic.Field(alias="pcfId")
    ] = None
    pcf_am_policy_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="pcfAmPolicyUri"), pydantic.Field(alias="pcfAmPolicyUri")
    ] = None
    am_policy_req_trigger_list: typing_extensions.Annotated[
        typing.Optional[typing.List[AmPolicyReqTrigger]],
        FieldMetadata(alias="amPolicyReqTriggerList"),
        pydantic.Field(alias="amPolicyReqTriggerList"),
    ] = None
    hpcf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hpcfId"), pydantic.Field(alias="hpcfId")
    ] = None
    restricted_rat_list: typing_extensions.Annotated[
        typing.Optional[typing.List[RatType]],
        FieldMetadata(alias="restrictedRatList"),
        pydantic.Field(alias="restrictedRatList"),
    ] = None
    forbidden_area_list: typing_extensions.Annotated[
        typing.Optional[typing.List[Area]],
        FieldMetadata(alias="forbiddenAreaList"),
        pydantic.Field(alias="forbiddenAreaList"),
    ] = None
    service_area_restriction: typing_extensions.Annotated[
        typing.Optional[ServiceAreaRestriction],
        FieldMetadata(alias="serviceAreaRestriction"),
        pydantic.Field(alias="serviceAreaRestriction"),
    ] = None
    restricted_core_nw_type_list: typing_extensions.Annotated[
        typing.Optional[typing.List[CoreNetworkType]],
        FieldMetadata(alias="restrictedCoreNwTypeList"),
        pydantic.Field(alias="restrictedCoreNwTypeList"),
    ] = None
    event_subscription_list: typing_extensions.Annotated[
        typing.Optional[typing.List[AmfEventSubscription]],
        FieldMetadata(alias="eventSubscriptionList"),
        pydantic.Field(alias="eventSubscriptionList"),
    ] = None
    mm_context_list: typing_extensions.Annotated[
        typing.Optional[typing.List[MmContext]],
        FieldMetadata(alias="mmContextList"),
        pydantic.Field(alias="mmContextList"),
    ] = None
    session_context_list: typing_extensions.Annotated[
        typing.Optional[typing.List[PduSessionContext]],
        FieldMetadata(alias="sessionContextList"),
        pydantic.Field(alias="sessionContextList"),
    ] = None
    trace_data: typing_extensions.Annotated[
        typing.Optional[TraceData], FieldMetadata(alias="traceData"), pydantic.Field(alias="traceData")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
